
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


black = [0,0,0]
p = 2.5         //larghezza/diametro pilastro standard
h = 25.0			//altezza dei pilastri
dpx = 25.0        //distanza tra un pilastro e l'altro su x
dpy = 48.75		//distanza tra un pilastro e l'altro su y
dpz = 3.0         //distanza tra un pilastro e l'altro su z (cioè lo spessore dei piani)
my = 11.25		//margine verticale
stepx = 2.5 	//pedata gradino
stepy = 8.75	//larghezza gradino


window_large_north = COLOR(black)(T([1,2,3])([dpx*4+p*4+p/3,p,dpz+h+dpz+h/2])(CUBOID([p/3,dpy,h/2-3])))

windows_large_north = STRUCT(NN(3)([window_large_north,T([3])([dpz+h])]))

window_thin_north = COLOR(black)(T([1,2,3])([dpx*4+p*4+p/3,p+dpy+my-p,dpz+h+dpz])(CUBOID([p/3,p,h])))

windows_thin_north = STRUCT(NN(3)([window_thin_north,T([3])([dpz+h])]))

windows_north = STRUCT([windows_large_north, windows_thin_north])

building = STRUCT([windows_north, wall, building_pillars, building_floors])

VIEW(building)