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

p = 2.5         //larghezza/diametro pilastro standard
h = 25.0			//altezza dei pilastri
dpx = 25.0        //distanza tra un pilastro e l'altro su x
dpy = 48.75		//distanza tra un pilastro e l'altro su y
dpz = 3.0         //distanza tra un pilastro e l'altro su z (cioè lo spessore dei piani)
my = 11.25		//margine verticale
stepx = 2.5 	//pedata gradino
stepy = 8.75	//larghezza gradino


function arc (alpha, r, R) {

	var domain = DOMAIN([[0,alpha],[r,R]])([36,1]);

	var mapping = function (v) {
		var a = v[0];
		var r = v[1];
		return [r*COS(a), r*SIN(a)];
	}

	var model = MAP(mapping)(domain);

	return model;
}

wall0_north = STRUCT([GRID([[67.5,-5,10],[p],[h]]), GRID([[-67.5,5,-10],[p],[17,-5,3]])])

wall0_west = STRUCT([GRID([[p],[-26.25,p,-7.5,1.25],[h]]), GRID([[p],[26.25],[h/2,-(h/2-3),3]]), GRID([[p],[-26.25,p,7.5],[-20,5]])])

wall0_east_unf = STRUCT([GRID([[p],[p,7.5,-7.5,p,-20,p],[h]]), GRID([[p],[-p,-7.5,7.5],[-20,h-20]]), GRID([[-p,15],[-p,-15,p,-20,p],[h]])])

round_wall_east = T([2])([12.5])(R([1,2])(-PI/2)(arc(PI, 10, 12.5)))

round_wall_east_3D = EXTRUDE([h])(round_wall_east)

wall0_east = STRUCT([wall0_east_unf, T([1,2])([p+15,p+15])(round_wall_east_3D)])

wall0_south_unf = STRUCT([GRID([[p,-7.5,p,p,dpx,p],[-6.25,-3.75,p],[h]]), GRID([[-p,-7.5,-p,-p,-dpx,-p,dpx],[-6.25,-3.75,p],[h/2,-(h/2-3),3]]), GRID([[p,-7.5,p],[-6.25,3.75],[h]])])

round_wall_south = T([1,2])([6.25,6.25])(R([1,2])(PI)(arc(PI, 3.75, 6.25)))

round_wall_south_3D = EXTRUDE([h])(round_wall_south)

wall0_south = STRUCT([wall0_south_unf,round_wall_south_3D])

wn = T([2])([p+dpy+p+8.75])(wall0_north)

ww = T([1,2])([12.5,p*3+17.5])(wall0_west)

ws = T([1,2])([12.5,12.5])(wall0_south)

we = T([1,2])([p*2+dpx*3,p+20])(wall0_east)

wall0 = STRUCT([wn,ww,ws,we])



wall1_north = T([2,3])([p+dpy+my,h+dpz])(STRUCT([GRID([[p*5+dpx*2,-dpx,dpx],[p],[h]]), GRID([[-p*5,-dpx*2,dpx],[p],[h/2,-(h/2-3),3]])]))

wall2_north = T([2,3])([p+dpy+my,h*2+dpz*2])(STRUCT([GRID([[p*4+dpx*3,p*2,-p,p*2,-p,p*5],[p],[h]]), GRID([[-p*4-dpx*3,-p*2,p,-p*2,p,-p*5],[p],[h/2,-(h/2-3),3]])]))

wall3_north = T([2,3])([p+dpy+my,h*3+dpz*3])(STRUCT([GRID([[-p*2,-dpx*2,p*3,dpx*2],[p],[h]]), GRID([[p*2,dpx*2],[-p/2,p/2],[h]])]))

wall1_2_3_north = STRUCT([wall1_north,wall2_north,wall3_north])



wall1_2_3_east = T([1,2,3])([p*4+dpx*4,p,dpz+h])(STRUCT(NN(3)([GRID([[p],[-dpy,-p,my-p*2],[h]]), GRID([[p],[dpy],[h/2,-(h/2-3),3]]),T([3])([h+dpz])])))



wall1_2_south = STRUCT(NN(2)([GRID([[p*3+dpx*2,-dpx,p*2+dpx],[p],[h+dpz]]), GRID([[-p*3,-dpx*2,dpx],[p],[h/2,-(h/2-3),3]]), T([3])([h+dpz])]))

wall3_south = STRUCT([GRID([[-p*3,-dpx*3,p*2,dpx],[p],[h]]), GRID([[p*3,dpx*3],[p],[h/2,-(h/2-3),3,dpz]])])

wall1_2_3_south = STRUCT([T([3])([dpz+h])(wall1_2_south), T([3])([dpz*3+h*3])(wall3_south)])



wall1_balcony = T([1,2])([-11,p+dpy+p/2])(STRUCT([GRID([[p/2],[10],[h/2]]), GRID([[-p/2,11-p/2],[p/3,-(10-p/3*2),p/3],[h/2]])]))

wall1_west = STRUCT([GRID([[p],[-p,-dpy,p,-7.5,1.25],[h]]), GRID([[p],[-p,-dpy,-p,7.5],[-20,5]]), GRID([[p],[-p,dpy],[-h,dpz]]), wall1_balcony])

wall2_west = GRID([[p],[-p,-dpy,p,my-p],[h]])

wall3_west = GRID([[p],[-p,dpy,my,p/2],[h/2,-(h/2-3),3,dpz]])

wall1_2_3_west = STRUCT([T([3])([dpz+h])(wall1_west),T([3])([dpz*2+h*2])(wall2_west),T([3])([dpz*3+h*3])(wall3_west)])


wall = T([3])([dpz])(STRUCT([wall0, wall1_2_3_north,wall1_2_3_east,wall1_2_3_south, wall1_2_3_west]))

building = STRUCT([wall, building_pillars, building_floors])

VIEW(building)