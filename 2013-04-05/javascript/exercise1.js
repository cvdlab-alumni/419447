T = function (dims) {
	dims = dims.map(function (item) {
		return item - 1;
	})
	return function (values) {
		return function (object) {
			return object.clone().translate(dims, values);
		}
	}
}

R = function (dims) {
	dims = dims.map(function (item) {
		return item - 1;
	})
	return function (values) {
		return function (object) {
			return object.clone().rotate(dims, values);
		}
	}
}

S = function (dims) {
	dims = dims.map(function (item) {
		return item - 1;
	})
	return function (values) {
		return function (object) {
			return object.clone().scale(dims, values);
		}
	}
}

S3 = S2
S2 = S1
S1 = S0

GRID = SIMPLEX_GRID

VIEW = DRAW

NN = REPLICA


//definisco una funzione CYLINDER che abbia lo stesso comportamento della corrispettiva in python
CYLINDER = function (params) {
	var R = params[0];
	var h = params[1];
	return function (dims) {
		var domain = DOMAIN([[0,2*PI], [0,R]])([dims, 1]);
		var mapping = function (v) {
			var a = v[0];
			var r = v[1];
			return [r*COS(v[0]),r*SIN(v[0])]
		}
		var circle = MAP(mapping)(domain);
		return EXTRUDE([h])(circle)
	}
}

//misure

var p = 2.5         //larghezza/diametro pilastro standard
var h = 25			//altezza dei pilastri
var dpx = 25        //distanza tra un pilastro e l'altro su x
var dpy = 48.75		//distanza tra un pilastro e l'altro su y
var dpz = 3         //distanza tra un pilastro e l'altro su z (cioè lo spessore dei piani)



var round_pillar = T([1,2])([p/2,p/2])(CYLINDER([p/2,h])(60))

var tiny_square_pillar = CUBOID([1.5,1.5,h])

var square_pillar = CUBOID([p,p,h])


//pilastri piano terra

var rp_nw = T([2])([p+dpy])(round_pillar)	//pilastro rotondo a nord ovest

var rp_ne = T([1])([p*4+dpx*4])(rp_nw)		//pilastro rotondo a nord est

var rps_south = STRUCT(NN(5)([round_pillar,T([1])([p+dpx])]))	//pilastri rotondi a sud

var round_pillars = STRUCT([rps_south,rp_nw,rp_ne])				//tutti i pilastri rotondi

var square_pillars = T([1,2])([p+dpx,p+dpy])(STRUCT(NN(3)([square_pillar,T([1])([p+dpx])])))	//tutti i pilastri quadrati

var pillars0 = STRUCT([round_pillars, square_pillars])			//pilastri piano terra


//pilastri primo piano

var square_pillars_f1 = GRID([[-p,-dpx,-p,-dpx,p,-dpx,-p,-dpx,p],[p,-dpy,p],[-h,-dpz,h]])	//schiera di pilastri simmetrici

var long_square_pillars_f1 = GRID([[p,-dpx,p],[p,-dpy,p],[-h,-dpz,2*h+dpz]])				//colonne lunghe

var lone_square_pillar_f1 = T([1,3])([3*p+3*dpx,h+dpz])(square_pillar)						//pilastro quadrato solitario

var lone_round_pillar_f1 = T([1,2,3])([3*p+3*dpx,p+dpy,h+dpz])(round_pillar)				//pilastro rotondo solitario

var pillars1 = STRUCT([square_pillars_f1,long_square_pillars_f1,lone_round_pillar_f1,lone_square_pillar_f1])		//pilastri primo piano


//pilastri secondo piano

var square_pillars_f2 = GRID([[p,-dpx,p,-dpx,-p,-dpx,-p,-dpx,p],[p,-dpy,p],[-h,-dpz,-h,-dpz,h]])	//schiera di pilastri quadrati simmetrici

var lone_square_pillars_f2 = T([1,2,3])([p*2+dpx*2,p+dpy,h*2+dpz*2])(STRUCT(NN(2)([square_pillar,T([1])([p+dpx])])))	//pilastro quadrato solitario

var pillars2 = STRUCT([square_pillars_f2, lone_square_pillars_f2])		//pilastri secondo piano


//pilastri terzo piano

var tiny_square_pillar_f3 = T([2,3])([p+dpy+0.5,h*3+dpz*3])(tiny_square_pillar)		//pilastro piccolo spostato al terzo piano, per comodità

var square_pillar_f3 = T([3])([h*3+dpz*3])(square_pillar)							//pilastro quadrato spostato al terzo piano, per comodità

var square_pillars_f3 = GRID([[-p,-dpx,-p,-dpx,p,-dpx,-p,-dpx,p],[p,-dpy,p],[-h,-dpz,-h,-dpz,-h,-dpz,h]])	//schiera di pilastri quadrati simmetrici

var lone_square_pillar_f3 = T([1,2])([dpx*3+p*3,p+dpy])(square_pillar_f3)			//pilastro quadrato solitario

var tiny_square_pillars_f3 = STRUCT(NN(2)([(tiny_square_pillar_f3),T([1])([p+dpx])]))	//coppia di pilastri piccoli

var pillars3 = STRUCT([square_pillars_f3, lone_square_pillar_f3, tiny_square_pillars_f3])	//pilastri terzo piano


//tutti i pilastri

var building_pillars = T([3])([dpz])(STRUCT([pillars0, pillars1, pillars2, pillars3]))

VIEW(building_pillars)
