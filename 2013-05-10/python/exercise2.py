def GRID(args):
	model = ([[]],[[0]])
	for k,steps in enumerate(args):
		model = larExtrude(model,steps*[1])
	V,cells = model
	verts = AA(list)(scipy.array(V)/AA(float)(args))
	return MKPOL([verts,AA(AA(lambda h:h+1))(cells),None])

def DOMAIN(dims):
	def DOMAIN0(divs):
		g = GRID(divs)
		i = 1
		for item in dims:
			a = item[0]
			b = item[1]
			g = T([i])([a])(SCALE([i])([b-a])(g))
			i = i+1
		return g
	return DOMAIN0

def translatePoints(values):
	x = values[0]
	y = values[1]
	z = values[2]
	def translatePoints0(points):
		p = []
		for a in points:
			c = [0,0,0]
			c[0] = a[0]+x
			c[1] = a[1]+y
			c[2] = a[2]+z
			p.append(c)
		return p
	return translatePoints0

def scalePoints(values):
	x = values[0]
	y = values[1]
	z = values[2]
	def scalePoints0(points):
		p = []
		for a in points:
			c = [0,0,0]
			c[0] = a[0]*x
			c[1] = a[1]*y
			c[2] = a[2]*z
			p.append(c)
		return p
	return scalePoints0

#LATO

p0 = [[1.29, 3.79], [1.2, 5.23], [2.73, 4.96], [2.57, 3.73]]
c0 = BEZIER(S1)(p0)
l0 = MAP(c0)(INTERVALS(1)(30))


p1 = [[1.29, 3.79], [0.11, 3.78], [0.11, 3.83], [0.17, 3.85], [0.15, 3.96], [0.17,4.22], [0.12,4.29]]
l1 = POLYLINE(p1)

p2 = [[0.12, 4.29], [0.35, 4.6], [1.17, 4.83], [1.67, 4.99]]
c2 = BEZIER(S1)(p2)
l2 = MAP(c2)(INTERVALS(1)(30))


p3 = [[1.67, 4.99],[1.76, 4.99], [1.86, 5]]
l3 = POLYLINE(p3)

p4 = [[1.86, 5], [2.66, 5.31], [3, 5.33], [3.44, 5.45]]
c4 = BEZIER(S1)(p4)
l4 = MAP(c4)(INTERVALS(1)(30))

p5 = [[5.23, 5.49], [4.61, 5.57], [4.08, 5.6], [3.44, 5.45]]
c5 = BEZIER(S1)(p5)
l5 = MAP(c5)(INTERVALS(1)(30))

p6 = [[5.23, 5.49], [6.27, 5.41], [7.5, 5.18], [7.88, 5.14]]
c6 = BEZIER(S1)(p6)
l6 = MAP(c6)(INTERVALS(1)(30))

p7 = [[7.88, 5.14], [7.96, 5.04], [8.04, 5.07], [8.09, 4.82]]
c7 = BEZIER(S1)(p7)
l7 = MAP(c7)(INTERVALS(1)(30))

p8 = [[8.09, 4.82], [8.03, 4.79], [8.15, 4.45], [8.18, 4.47], [8.18, 4.25], [7.34, 3.81]]
l8 = POLYLINE(p8)

p9 = [[5.99, 3.73], [5.77, 5.15], [7.41, 5.11], [7.34, 3.81]]
c9 = BEZIER(S1)(p9)
l9 = MAP(c9)(INTERVALS(1)(30))

p10 = [[2.57, 3.73],[5.99, 3.73]]
l10 = POLYLINE(p10)

lato = T([1,2])([-0.11,-3.73])(STRUCT([l0,l1,l2,l3,l4,l5,l6,l7,l8,l9,l10]))
lato_xz = R([2,3])(PI/2)(lato)

#FRONTE

p0 = [[0.43, 4.11], [4.03, 4.11]]
c0 = BEZIER(S1)(p0)
f0 = MAP(c0)(INTERVALS(1)(30))

p1 = [[0.43, 4.11], [0.32, 4.31], [0.36, 4.82], [0.34, 5.13]]
c1 = BEZIER(S1)(p1)
f1 = MAP(c1)(INTERVALS(1)(30))

p2 = [[0.34, 5.13], [0.44, 5.31], [0.45, 5.32], [0.58, 5.39]]
c2 = BEZIER(S1)(p2)
f2 = MAP(c2)(INTERVALS(1)(30))

p3 = [[0.58, 5.39], [0.64, 5.58], [0.98, 5.67], [1.06, 5.71]]
c3 = BEZIER(S1)(p3)
f3 = MAP(c3)(INTERVALS(1)(30))

p4 = [[1.06, 5.71], [1.19, 5.92], [3.28, 5.92], [3.32, 5.71]]
c4 = BEZIER(S1)(p4)
f4 = MAP(c4)(INTERVALS(1)(30))

p5 = [[3.32, 5.71], [3.40,5.67], [3.82,5.58], [3.88, 5.39]]
c5 = BEZIER(S1)(p5)
f5 = MAP(c5)(INTERVALS(1)(30))

p6 = [[3.88, 5.39], [4.01,5.32], [4.02,5.31], [4.12,5.16]]
c6 = BEZIER(S1)(p6)
f6 = MAP(c6)(INTERVALS(1)(30))

p7 = [[4.12,5.16], [4.10,4.82], [4.14,4.31], [4.03,4.11]]
c7 = BEZIER(S1)(p7)
f7 = MAP(c7)(INTERVALS(1)(30))

fronte = T([1,2])([-4.12,-4.11])(STRUCT([f0,f1,f2,f3,f4,f5,f6, f7]))
fronte_xz = R([2,3])(PI/2)(fronte)
fronte_yz = R([1,2])(-PI/2)(fronte_xz)


#TETTO

p0 = [[0.29, 2.71], [0, 3.26], [0, 4.56], [0.32, 5.04]]
c0 = BEZIER(S1)(p0)
t0 = MAP(c0)(INTERVALS(1)(30))

p1 = [[0.32, 5.04], [0.38, 5.18], [0.45, 5.28], [1.04, 5.44]]
c1 = BEZIER(S1)(p1)
t1 = MAP(c1)(INTERVALS(1)(30))

p2 = [[1.04, 5.44], [1.27, 5.61], [2.14, 5.5], [2.74, 5.54]]
c2 = BEZIER(S1)(p2)
t2 = MAP(c2)(INTERVALS(1)(30))

p3 = [[2.73, 5.54], [2.82, 5.44], [4.27, 5.46], [5.89, 5.63]]
c3 = BEZIER(S1)(p3)
t3 = MAP(c3)(INTERVALS(1)(30))

p4 = [[5.89, 5.63], [7.25, 5.61], [7.78, 5.44], [7.79, 5.37]]
t4 = POLYLINE(p4)

p5 = [[7.8, 5.38], [7.98, 5.35], [8.14, 5.02], [8.16, 3.83]]
c5 = BEZIER(S1)(p5)
t5 = MAP(c5)(INTERVALS(1)(30))

p6 = [[8.16, 3.83], [8.13, 3.04], [8.07, 2.25], [7.77, 2.24]]
c6 = BEZIER(S1)(p6)
t6 = MAP(c6)(INTERVALS(1)(30))

p7 = [[7.77, 2.24], [7.76, 2.18], [7.24, 2.02], [5.91, 2]]
t7 = POLYLINE(p7)

p8 = [[5.91, 2], [4.54, 2.13], [2.8, 2.25], [2.72, 2.11]]
c8 = BEZIER(S1)(p8)
t8 = MAP(c8)(INTERVALS(1)(30))

p9 = [[2.72, 2.11], [2.02, 2.17], [1.37, 2.01], [1, 2.22]]
c9 = BEZIER(S1)(p9)
t9 = MAP(c9)(INTERVALS(1)(30))

p10 = [[1, 2.22], [0.63, 2.4], [0.35, 2.39], [0.29, 2.71]]
c10 = BEZIER(S1)(p10)
t10 = MAP(c10)(INTERVALS(1)(30))

tetto = T(2)(-2)(STRUCT([t0,t1,t2,t3,t4,t5,t6,t7,t8,t9,t10]))


crime_scene_mode = STRUCT([
			lato_xz,
			fronte_yz,
			tetto])
#VIEW(crime_scene_mode)



fronte_c = T(1)(8.16/2)(fronte_yz)
lato_c = T([1,2])([0.11,3.63/2])(lato_xz)
tetto_c = T(3)(4.29-3.73)(tetto)

center_mode = STRUCT([fronte_c, lato_c, tetto_c])

VIEW(center_mode)