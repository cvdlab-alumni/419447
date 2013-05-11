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

def rim (in_radius, rim_height):

		dom1 = INTERVALS(2*PI)(80)
		dom2 = T(1)(in_radius)(INTERVALS(rim_height)(1))
		domain = PROD([dom1, dom2])

		def mapping (v):
			
			a = v[0]
			r = v[1]
			return [r*COS(a), r*SIN(a)]

		model = MAP(mapping)(domain)

		rim = PROD([model, Q(6)])

		return rim

def hub (hub_radius_in, hub_radius_out):

		dom1 = INTERVALS(2*PI)(80)
		dom2 = T(1)(hub_radius_in)((INTERVALS(hub_radius_out-hub_radius_in)(1)))
		dom3 = (INTERVALS(hub_radius_in)(1))
		domain1 = PROD([dom1, dom2])
		domain2 = PROD([dom1, dom3])

		def mapping (v):
			a = v[0]
			r = v[1]
			return [r*COS(a), r*SIN(a)]

		model1 = MAP(mapping)(domain1);
		model2 = MAP(mapping)(domain2);

		hub = STRUCT([PROD([model1, Q(5)]),COLOR(GRAY)(PROD([model2,Q(4.5)]))])

		return hub

def torus(R, r):
	def torus0(v):
		a = v[0]
		b = v[1]

		u = (r*COS(a)+R)*COS(b)
		v = (r*COS(a)+R)*SIN(b)
		w = (r*SIN(a))

		return [u,v,w]
	return torus0

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


#EXERCISE 3:
#RUOTE


dom = INTERVALS(1)(30)
dom2D = DOMAIN([[0,1],[0,2*PI]])([40,40])
p = [[0,0,0],[5,0,0],[0,0,3],[5,0,6],[0,0,6]]
p = translatePoints([5,0,0])(p)
c = BEZIER(S1)(p)
tire = COLOR(BLACK)(MAP(ROTATIONALSURFACE(c))(dom2D))

rim = rim(4.9,0.1)

hub = hub(0.7,1.1)

#RAY
dom2D = GRID([30,30])#[0.6,0,0.7],[3,0,1],[4,0,1]
p0 = [[0,0,0],[1.2,0,0]]
r0 = BEZIER(S1)(p0)
p1 = [[-1.6,4,1],[2.8,4,1]]#translatePoints([0,4,1])(p0)
r1 = BEZIER(S1)(p1)
p2 = [[0,0,0],[1.2,0.6,0.7],[-0.4,3,1],[-1.6,4,1]]
r2 = BEZIER(S2)(p2)
p3 = [[1.2,0,0],[0,0.6,0.7],[1.6,3,1],[2.8,4,1]]#translatePoints([2,0,0])(p2)
r3 = BEZIER(S2)(p3)
#out = STRUCT([MAP(c0)(dom2D),MAP(c1)(dom2D),MAP(c2)(dom2D),MAP(c3)(dom2D)])

surface = COONSPATCH([r0,r1,r2,r3])
solidMapping = THINSOLID(surface)
domain3D = PROD([PROD([INTERVALS(1)(10),INTERVALS(1)(10)]),INTERVALS(0.5)(1)])
ray = T([1,2])([-0.6,1])(S([1,2,3])([1./3,1./3,1./3])(MAP(solidMapping)(domain3D)))


p4 = [[0,0,0],[0.4,0,0]]
r4 = BEZIER(S1)(p4)
p5 = [[-1.6,4,1],[0.4,4,1]]#translatePoints([0,4,1])(p0)
r5 = BEZIER(S1)(p5)
p6 = [[0,0,0],[1.2,0.6,0.7],[-0.4,3,1],[-1.6,4,1]]
r6 = BEZIER(S2)(p6)
p7 = [[0.4,0,0],[0.4,0.6,0.7],[0.4,3,1],[0.4,4,1]]#translatePoints([2,0,0])(p2)
r7 = BEZIER(S2)(p7)

surface = COONSPATCH([r4,r5,r6,r7])
solidMapping = THINSOLID(surface)
domain3D = PROD([PROD([INTERVALS(1)(10),INTERVALS(1)(10)]),INTERVALS(0.5)(1)])
mini_ray_left = T([1,2])([-0.6,1])(S([1,2,3])([1./3,1./3,1./3])(MAP(solidMapping)(domain3D)))


p8 = [[0.8,0,0],[1.2,0,0]]
r8 = BEZIER(S1)(p8)
p9 = [[0.8,4,1],[2.8,4,1]]
r9 = BEZIER(S1)(p9)
p10= [[0.8,0,0],[0.8,0.6,0.7],[0.8,3,1],[0.8,4,1]]
r10 = BEZIER(S2)(p10)
p11= [[1.2,0,0],[0,0.8,0.7],[1.6,3,1],[2.8,4,1]]
r11 = BEZIER(S2)(p11)
surface = COONSPATCH([r8,r9,r10,r11])
solidMapping = THINSOLID(surface)
domain3D = PROD([PROD([INTERVALS(1)(10),INTERVALS(1)(10)]),INTERVALS(0.5)(1)])
mini_ray_right = T([1,2])([-0.6,1])(S([1,2,3])([1./3,1./3,1./3])(MAP(solidMapping)(domain3D)))

mini_ray = STRUCT([mini_ray_left,mini_ray_right])

#VIEW(ray)
rays = T(3)(5-0.3)(STRUCT(NN(5)([ray, R([1,2])(2*PI/5)])))
mini_rays = COLOR(GRAY)(T(3)(5-0.2)(STRUCT(NN(5)([mini_ray, R([1,2])(2*PI/5)]))))

all_rays = STRUCT([mini_rays, rays])

wheel_big = STRUCT([hub, rim, tire, all_rays])

wheel = S([1,2,3])([1./12,1./12,1./12])(wheel_big)

left_wheel = R([2,3])(PI/2)(wheel)
right_wheel = R([2,3])(-PI/2)(wheel)

front_left_wheel = T([1,3])([1.81,0.4])(left_wheel)
back_left_wheel = T([1,3])([6.49,0.4])(left_wheel)
front_right_wheel = T([1,2,3])([1.81,3.65,0.4])(right_wheel)
back_right_wheel = T([1,2,3])([6.49,3.65,0.4])(right_wheel)
wheels = STRUCT([front_left_wheel, back_left_wheel, back_right_wheel, front_right_wheel])


#EXERCISE3
#VOLANTE

domain_torus = DOMAIN([[0,2*PI],[0,2*PI]])([40,50]);

torus_model = T(3)(2.5)(MAP(torus(6,0.7))(domain_torus))

p0 = [[0,0,0],[0.5,0,0]]
v0 = BEZIER(S1)(p0)
p1 = translatePoints([0,6,2.5])([[0.5,0,0],[1,0,0]])
v1 = BEZIER(S1)(p1)
p2 = [[0,0,0],[0.2,2,0],[0.3,3.5,0],[0.5,6,2.5]]
v2 = BEZIER(S2)(p2)
p3 = translatePoints([0.5,0,0])(p2)
v3 = BEZIER(S2)(p3)

#first = MAP(COONSPATCH([v0,v1,v2,v3]))(GRID([20,20]))
first_map = THINSOLID(COONSPATCH([v0,v1,v2,v3]))
first = MAP(first_map)(domain3D)

p4 = [[1,0,0],[1.5,0,0]]
v4 = BEZIER(S1)(p4)
p5 = translatePoints([0,6,2.5])([[0.8,0,0],[1.3,0,0]])
v5 = BEZIER(S1)(p5)
p6 = [[1,0,0],[1.1,2,0],[1,3.5,0],[0.8,6,2.5]]
v6 = BEZIER(S2)(p6)
p7 = translatePoints([0.5,0,0])(p6)
v7 = BEZIER(S2)(p7)

#second = MAP(COONSPATCH([v4,v5,v6,v7]))(GRID([20,20]))
second_map = THINSOLID(COONSPATCH([v4,v5,v6,v7]))
second = MAP(second_map)(domain3D)

razza = T(1)(-0.75)(S([1,2,3])([1./3,1./3,1./3])(STRUCT([first, second])))

razze = STRUCT(NN(3)([razza, R([1,2])(-PI/2)]))

pomo1 = COLOR(GRAY)(PROD([CIRCLE(1)([30,1]),Q(0.4)]))
pomo2 = T(3)(0.4)(PROD([CIRCLE(0.6)([30,1]),Q(0.1)]))
pomo = T(3)(0)(STRUCT([pomo1,pomo2]))

steering_wheel_big = STRUCT([razze, torus_model, pomo])

steering_wheel_rot = R([1,3])(-PI/3)(S([1,2,3])([1./20,1./20,1./20])(steering_wheel_big))

steering_wheel = T([1,2,3])([2.76,1.3,1.1])(steering_wheel_rot)

whole = STRUCT([center_mode, wheels, steering_wheel])

VIEW(whole)