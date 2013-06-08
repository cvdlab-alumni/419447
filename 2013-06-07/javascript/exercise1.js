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

out = STRUCT([terrain_model]);

DRAW(out);