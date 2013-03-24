function Edge(a,b) {
	this.a = a;
	this.b = b;
	this.length = function() {
		 return Math.sqrt(Math.pow((this.b.x-this.a.x),2) + Math.pow((this.b.y-this.a.y),2));
	}
}

