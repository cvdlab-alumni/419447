function exports(lar_model){
	V = lar_model[0];
	FV = lar_model[1];
	res +="# Vertici:"+"\n";
	for (var i = 0; i < V.length; i++){
			res += "V "+V[i][0]+" "+V[i][1]+" "+V[i][2]+" "+V[i][3]+"\n";
	}
	output += "# acce:"+"\n";
	res += "f " +FV[0][0]+FV[0][1]+FV[0][2];
	for (var j=1; j<FV.length;j++){
		res+= FV[j][0]+"/"+FV[j][1]+"/"+FV[j][2]+"\n";
	}
return res;
}