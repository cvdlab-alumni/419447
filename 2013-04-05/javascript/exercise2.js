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

var p = 2.5
var h = 25
var dpx = 25
var dpy = 48.75
var dpz = 3
var my = 11.25		//margine verticale
var stepx = 2.5 	//pedata gradino
var stepy = 8.75	//larghezza gradino

//pavimento fondazioni
var floor0 = CUBOID([p*5+dpx*4,p*2+dpy+my,dpz])

VIEW(floor0)

//primo piano senza balcone
var f1_minus_balcony = STRUCT([GRID([[p*5+dpx*4],[p*2+dpy,-stepy,p],[dpz]]),
							   GRID([[27.5,-stepx*13,52.5],[-p*2,-dpy,stepy],[dpz]])])

var balcony = CUBOID([11,10,2.5])

var floor1 = STRUCT([f1_minus_balcony, T([1,2,3])([-11,52.5,0.5])(balcony)])


//piano due, senza alcune sezioni
var floor2_unfinished = STRUCT([GRID([[-p*2,-dpx*2,p*3,dpx*2],[p*2,dpy],[dpz]]),
								GRID([[15,-stepx*13,p*5 + dpx*4 - 15 - stepx*13],[-p*2,-dpy,stepy],[dpz]]),
								GRID([[p*5,dpx*4],[-p,-dpy,-my,p],[dpz]])])

var points = [[p*2+dpx*2,p],[p*2+dpx*2,p*2+dpy],[45,p*2+dpy]]

var f2_part_2D = SIMPLICIAL_COMPLEX(points)([[0,1,2]])
//sezione triangolare 3D
var f2_part_3D = EXTRUDE([dpz])(f2_part_2D)
//piano due completo
var floor2 = STRUCT([f2_part_3D,floor2_unfinished])




var floor3 = STRUCT([GRID([[p*5+dpx*4],[p*2+dpy,-stepy,p],[dpz]]),
					 GRID([[p*2+dpx*2,-stepx*13,p*5 + dpx*4 - p*2 - dpx*2 - stepx*13],[-p*2,-dpy,stepy],[dpz]])])




var floor4 = STRUCT([GRID([[-p*2,-dpx*2,p*3,dpx*2],[p,dpy],[dpz]]),
					 GRID([[p*5,dpx*4],[-p,-dpy,p,my],[dpz]])])



var building_floors = STRUCT([floor0, T([3])([h+dpz])(floor1), T([3])([h*2+dpz*2])(floor2), T([3])([h*3+dpz*3])(floor3), T([3])([h*4+dpz*4])(floor4)])

VIEW(building_floors)

