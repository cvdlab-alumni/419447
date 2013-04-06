p = 2.5
h = 25
dpx = 25
dpy = 48.75
dpz = 3
my = 11.25		#margine verticale
stepx = 2.5 	#pedata gradino
stepy = 8.75	#larghezza gradino

#pavimento fondazioni
floor0 = CUBOID([p*5+dpx*4,p*2+dpy+my,dpz])

#primo piano senza balcone
f1_minus_balcony = CUBOID([p*5+dpx*4,p*2+dpy+my,dpz])

balcony = CUBOID([11,10,2.5])

#vuoto per la scala primo piano
hollow_f1 = T([1,2])([27.5,53.75])(CUBOID([stepx*13,stepy,dpz]))

floor1 = STRUCT([DIFFERENCE([f1_minus_balcony, hollow_f1]), T([1,2,3])([-11,52.5,0.5])(balcony)])



f2 = f1_minus_balcony

hollow_f2 = T([1,2])([15,53.75])(CUBOID([stepx*13,stepy,dpz]))

hollow2_f2_2D = MKPOL([[[0,0],[p*2+dpx*2,0],[p*2+dpx*2,p],[15+stepx*12,p*2+dpy],[0,p*2+dpy]],[[1,2,3,4,5]],None])

hollow2_f2 = PROD([hollow2_f2_2D, Q(dpz)])

floor2_unfinished = DIFFERENCE([f2, hollow_f2])

floor2 = DIFFERENCE([floor2_unfinished, hollow2_f2])



f3 = f2

hollow_f3 = T([1,2])([p*2+dpx*2,53.75])(CUBOID([stepx*13,stepy,dpz]))

floor3 = DIFFERENCE([f3, hollow_f3])



f4 = f3

hollow_f4 = CUBOID([p*2+dpx*2,p+dpy,dpz])

floor4 = DIFFERENCE([f4, hollow_f4])

building_floors = STRUCT([floor0, T([3])([h+dpz])(floor1), T([3])([h*2+dpz*2])(floor2), T([3])([h*3+dpz*3])(floor3), T([3])([h*4+dpz*4])(floor4)])

building = STRUCT([building_pillars, building_floors])

VIEW(building)