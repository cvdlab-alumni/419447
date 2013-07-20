var COLS = 70;
var ROWS = 70;
var H = 4;
var scale_factor = [0.5,0.5,0.1];
var divs = 36;

var GREEN = [0,1,0];
var BROWN = [0.54,0.27,0.07];
var GOLDENROD = [0.85,0.65,0.12];
var GREY = [0.41,0.41,0.41];
var ORED = [1,0.27,0];

function getRandomArbitrary(min, max) {
  return Math.random() * (max - min) + min;
}

var z = function (u,v) {
	return ((SIN(u/4)+1)*Math.pow(u,4/3))*0.2 + ((COS(v/8)+1)*Math.pow(v,1.2)*0.1);//Math.pow(v,2)*0.05;
}

var coordinates_to_ordinal = function (cols) {
	return function (coordinates) {
		var row = coordinates[0];
		var column = coordinates[1];
		return row*cols+column;
	}
}

var ordinal_to_coordinates = function(point) {
	var row = point/ROWS
	var col = point/COLS
	return [row, col]
}

var get_point = function (points, coordinates) {
	return points[coordinates_to_ordinal(COLS)(coordinates)];
}

var check_coordinates = function (coordinates) {
	var row=coordinates[0]
	var col=coordinates[1]
	if ((col<COLS) && (row<ROWS) && (row>-1) && (col>-1)) {
		return [row,col]
	} else {
		return null
	}
}

var east = function (coordinates) {
	return check_coordinates([coordinates[0],coordinates[1]+1])
}

var west = function ( coordinates) {
	return check_coordinates([coordinates[0], coordinates[1]-1])	
}

var north = function (coordinates) {
	return check_coordinates([coordinates[0]-1, coordinates[1]])
}

var south = function (coordinates) {
	return check_coordinates([coordinates[0]+1, coordinates[1]])	
}

var complex_points = function(coordinates) {
	var points =[coordinates, east(coordinates), south(east(coordinates)), south(coordinates)]
	return points 
}

var complex_cells = function (complex_points) {
	var cells = [
				[complex_points[0],complex_points[1],complex_points[3]],
				[complex_points[1],complex_points[2],complex_points[3]]
				]
	return cells
}

var round = function (coordinates) {
	return [north(west(coordinates)), north(coordinates), north(east(coordinates)), 
			east(coordinates), 
			south(east(coordinates)), south(coordinates), south(west(coordinates)),
			west(coordinates)]
}

function coordinates_to_cells(rows_length, cols_length) {
	var my_cells = [];
	for (var i=0; i<rows_length-1; i++) {
		for (var j=0; j<cols_length-1; j++) {
			cs = complex_cells(complex_points([i,j]));
			my_cells.push(cs[0].map(coordinates_to_ordinal(cols_length)))
			my_cells.push(cs[1].map(coordinates_to_ordinal(cols_length)))
		}
	}
	return my_cells;
}

var cells = function (points_number, row_length) {
	var my_cells = [];
	for (var i=1; i<points_number-row_length; i++) {
		if ((i%row_length)!==0) {
			my_cells.push([i-1,i,i+row_length-1]);
			my_cells.push([i,i+row_length-1,i+row_length]);
		}
	}
	return my_cells;
}

var generate_points = function (rows_length, cols_length) {
	var row = [];
	for (var i=0; i<rows_length; i++) {
		for (var j=0; j<cols_length; j++) {
			row.push([i,j,1]);
		}
	}
	return row;
}

var c = coordinates_to_cells(ROWS, COLS);
var p = generate_points(ROWS, COLS);

p = p.map(function(e){e[2] = z(e[0],e[1])*scale_factor[2]; return e});
p = p.map(function(e){e[0]*=scale_factor[0]; e[1]*=scale_factor[1]; return e});
var points = p;

var terrain_model = COLOR(GOLDENROD)(SIMPLICIAL_COMPLEX(p)(c));

var lake = COLOR([0.4,0.8,0.67])(CUBOID([(2*ROWS/3)*scale_factor[1],(2*COLS/3)*scale_factor[0],H*scale_factor[2]]));

function conifer(h, r, divs) {
	var log = COLOR(BROWN)(EXTRUDE([2*h/3])(CIRCLE(r)(divs)));
	var ps = [[2*r,0,0],[0,0,2*h/3]]
	var dom = DOMAIN([[0,1],[0,2*PI]])([1,divs]);
	var fronds = COLOR(GREEN)(MAP(ROTATIONAL_SURFACE(BEZIER(S0)(ps)))(dom));
	var base_fronds = COLOR(GREEN)(DISK(2*r)(divs))
	return STRUCT([T([2])([-h/3])(log),T([2])([h/3])(fronds),T([2])([h/3])(base_fronds)]);
}

function forest(centro, r, treesnumber) {
	var woods = [];
	for (var i=0; i<treesnumber; i++) {
		var x = centro[0]+(Math.random()*r-r/2);
		var y = centro[1]+(Math.random()*r-r/2);
		var zeta = z(x,y);
		var tree = T([0,1,2])([x*scale_factor[0],y*scale_factor[1],zeta*scale_factor[2]])(conifer(1*scale_factor[0],0.1*scale_factor[0], divs));
		woods.push(tree);
	}
	return STRUCT(woods);
}


function house(coordinates) {
	var x = getRandomArbitrary(0.4, 0.9) * scale_factor[0]
	var y = getRandomArbitrary(0.4,0.9) * scale_factor[1]
	var z = 0.5+(getRandomArbitrary(0.5, 1) * scale_factor[2]);
	var roof0 = EXTRUDE([y])(SIMPLICIAL_COMPLEX([[0,0],[x,0],[x/2,0.3]])([[0,1,2]]));
	var roof = COLOR(ORED)(T([1,2])([y,z])(R([1,2])([PI/2])(roof0)));
	var house = STRUCT([CUBOID([x,y,z]), roof]);
	return T([0,1,2])(get_point(points, coordinates))(T([0,2])([-x,-z/3])(house));
}

function bunch_of_houses(centro) {
	var q = [];
	var coords = [south(centro),south(west(centro)),west(centro), centro];
	for (var i=0; i<coords.length; i++) {
		if (coords[i]!==null) {
			q.push(house(coords[i]));
		}
	}
	return STRUCT(q);
}

var out = STRUCT([lake, 
				  forest([25,50],7,40),forest([30,50],7,80),forest([32,8],5,60),
				  bunch_of_houses([10,7]),bunch_of_houses([10,10]),bunch_of_houses([10,13]),bunch_of_houses([10,16]),bunch_of_houses([12,50]),bunch_of_houses([12,53]),bunch_of_houses([15,53]),bunch_of_houses([9,50]),bunch_of_houses([9,53]),
				  terrain_model]);

DRAW(out);