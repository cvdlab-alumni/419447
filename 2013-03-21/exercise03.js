//Given the paramethers a, b and c are Edge objects

function Triangle(a,b,c) {
	this.a = a;
	this.b = b;
	this.c = c;
	this.perimether = function() {
		return this.a.length() + this.b.length() + this.c.length();
	}
	this.area = function() {
		var p = this.perimether()/2;
		return Math.sqrt(p*(p-this.a.length())*(p-this.b.length())*(p-this.c.length()));
	}
}