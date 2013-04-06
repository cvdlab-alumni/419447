p = 2.5
h = 25
dpx = 25
dpy = 48.75
dpz = 3
my = 11.25		#margine verticale
stepx = 2.5 	#pedata gradino
stepy = 8.75	#larghezza gradino
stepz = (h+dpz)/13

step2D = MKPOL([[[0,0],[0,dpz+stepz],[stepx,dpz+stepz],[stepx,stepz]],[[1,2,3,4]], None])

step3D = MAP([S1,S3,S2])(PROD([step2D, Q(stepy)]))

ramp = STRUCT(NN(13)([step3D,T([1,3])([stepx,stepz])]))

ramp1 = T([1,2])([15+dpx/2,p+dpy+p])(ramp)

ramp2 = T([1,2,3])([15+dpx/2,p+dpy+p])(ramp)

ramp3 = T([1,2,3])([15+dpx/2,p+dpy+p])(ramp)

building = STRUCT([ramp1, windows_north, wall, building_pillars, building_floors])

VIEW(building)