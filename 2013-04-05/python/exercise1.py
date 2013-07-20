
GRID = COMP([INSR(PROD),AA(QUOTE)])

#misure

p = 2.5         #larghezza/diametro pilastro standard
h = 25			#altezza dei pilastri
dpx = 25        #distanza tra un pilastro e l'altro su x
dpy = 48.75		#distanza tra un pilastro e l'altro su y
dpz = 3         #distanza tra un pilastro e l'altro su z (cioè lo spessore dei piani)



round_pillar = T([1,2])([p/2,p/2])(CYLINDER([p/2,h])(60))

tiny_square_pillar = CUBOID([1.5,1.5,h])

square_pillar = CUBOID([p,p,h])


#pilastri piano terra

rp_nw = T([2])([p+dpy])(round_pillar)	#pilastro rotondo a nord ovest

rp_ne = T([1])([p*4+dpx*4])(rp_nw)		#pilastro rotondo a nord est

rps_south = STRUCT(NN(5)([round_pillar,T([1])([p+dpx])]))	#pilastri rotondi a sud

round_pillars = STRUCT([rps_south,rp_nw,rp_ne])				#tutti i pilastri rotondi

square_pillars = T([1,2])([p+dpx,p+dpy])(STRUCT(NN(3)([square_pillar,T([1])([p+dpx])])))	#tutti i pilastri quadrati

pillars0 = STRUCT([round_pillars, square_pillars])			#pilastri piano terra


#pilastri primo piano

square_pillars_f1 = GRID([[-p,-dpx,-p,-dpx,p,-dpx,-p,-dpx,p],[p,-dpy,p],[-h,-dpz,h]])	#schiera di pilastri simmetrici

long_square_pillars_f1 = GRID([[p,-dpx,p],[p,-dpy,p],[-h,-dpz,2*h+dpz]])				#colonne lunghe

lone_square_pillar_f1 = T([1,3])([3*p+3*dpx,h+dpz])(square_pillar)						#pilastro quadrato solitario

lone_round_pillar_f1 = T([1,2,3])([3*p+3*dpx,p+dpy,h+dpz])(round_pillar)				#pilastro rotondo solitario

pillars1 = STRUCT([square_pillars_f1,long_square_pillars_f1,lone_round_pillar_f1,lone_square_pillar_f1])		#pilastri primo piano


#pilastri secondo piano

square_pillars_f2 = GRID([[p,-dpx,p,-dpx,-p,-dpx,-p,-dpx,p],[p,-dpy,p],[-h,-dpz,-h,-dpz,h]])	#schiera di pilastri quadrati simmetrici

lone_square_pillars_f2 = T([1,2,3])([p*2+dpx*2,p+dpy,h*2+dpz*2])(STRUCT(NN(2)([square_pillar,T([1])([p+dpx])])))	#pilastro quadrato solitario

pillars2 = STRUCT([square_pillars_f2, lone_square_pillars_f2])		#pilastri secondo piano


#pilastri terzo piano

tiny_square_pillar_f3 = T([2,3])([p+dpy+0.5,h*3+dpz*3])(tiny_square_pillar)		#pilastro piccolo spostato al terzo piano, per comodità

square_pillar_f3 = T([3])([h*3+dpz*3])(square_pillar)							#pilastro quadrato spostato al terzo piano, per comodità

square_pillars_f3 = GRID([[-p,-dpx,-p,-dpx,p,-dpx,-p,-dpx,p],[p,-dpy,p],[-h,-dpz,-h,-dpz,-h,-dpz,h]])	#schiera di pilastri quadrati simmetrici

lone_square_pillar_f3 = T([1,2])([dpx*3+p*3,p+dpy])(square_pillar_f3)			#pilastro quadrato solitario

tiny_square_pillars_f3 = STRUCT(NN(2)([(tiny_square_pillar_f3),T([1])([p+dpx])]))	#coppia di pilastri piccoli

pillars3 = STRUCT([square_pillars_f3, lone_square_pillar_f3, tiny_square_pillars_f3])	#pilastri terzo piano


#tutti i pilastri

building_pillars = T([3])([dpz])(STRUCT([pillars0, pillars1, pillars2, pillars3]))

VIEW(building_pillars)
