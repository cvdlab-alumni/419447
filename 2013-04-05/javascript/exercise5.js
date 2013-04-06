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


p = 2.5
h = 25
dpx = 25
dpy = 48.75
dpz = 3
my = 11.25		//margine verticale
stepx = 2.5 	//pedata gradino
stepy = 8.75	//larghezza gradino
stepz = (h+dpz)/13

points = [[0,0],[0,dpz+stepz],[stepx,dpz+stepz],[stepx,stepz]]
cells = [[0,1,3],[1,2,3]]

step2D = SIMPLICIAL_COMPLEX(points)(cells)

step3D = MAP([S1,S3,S2])(EXTRUDE([stepy])(step2D))

ramp = STRUCT(NN(13)([step3D,T([1,3])([stepx,stepz])]))

ramp1 = T([1,2])([15+dpx/2,p+dpy+p])(ramp)

VIEW(ramp1)