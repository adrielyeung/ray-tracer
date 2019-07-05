import raytracerfinal as rtf

# Test 1: through surface 1 surf1
newray = rtf.ray([0,0,-10-1./0.3],[0,0,1])
surf = rtf.SphericalRefraction(-1./0.3, 0.3, 0.1, 0.3, 20.)
surf.propagate_ray(newray)
print newray.vertices() # new point added
print newray.p() # new point replaced old
print newray.k() # remains the same

# Test 2: through a second surface surf2
surf2 = rtf.SphericalRefraction(10,0.2,1.5,1,2)
surf2.propagate_ray(newray)
print newray.vertices() # another point added
print newray.p()
print newray.k()

# Test 3: through surface 1 again (not possible!)
surf.propagate_ray(newray)
print newray._term # True --> terminated now

# Test 4: propagate parallel to surface
newray = rtf.ray([0,-10,-1./0.3],[0,1,0])
surf = rtf.SphericalRefraction(-1./0.3, 0.3, 1, 1.5, 1.)
surf.propagate_ray(newray)
print newray.vertices() # y-coord of new point ~ 0
print newray.k() # compare with Task 5 test

# Test 5: total internal reflection
newray = rtf.ray([0,-10,0],[0,1,1])
surf2.propagate_ray(newray)
print newray._term

# Test 6: Online example, see Task 5 test
surf = rtf.SphericalRefraction(0, 0.3, 1, 1.5, 2.)
newray = rtf.ray([-1,0,-1],[1,0,1])
surf.propagate_ray(newray)
print newray.vertices()
print newray.k()

# change curvature to -0.03 and 0 respectively for convex surface in other
# direction and plane

# Test 19: 4 parallel rays, see if they converge
surf1 = rtf.SphericalRefraction(19.9,0.03,1,1.5,3)
surf2 = rtf.SphericalRefraction(20.1,-0.03,1.5,1,3)
ray1 = rtf.ray([0,1,0],[0,0,1])
ray2 = rtf.ray([0,0,0],[0,0,1])
ray3 = rtf.ray([0,-1,0],[0,0,1])
surf1.propagate_ray(ray1)
surf2.propagate_ray(ray1)
surf1.propagate_ray(ray2)
surf2.propagate_ray(ray2)
surf1.propagate_ray(ray3)
surf2.propagate_ray(ray3)
print ray1.vertices()
print ray1.k()
print ray2.vertices()
print ray2.k()
print ray3.vertices()
print ray3.k()
ray4 = rtf.ray([0,0.5,0],[0,0,1])
surf1.propagate_ray(ray4)
surf2.propagate_ray(ray4)
ray4.vertices()
ray4.k()

# Test 20: reversing the above case, propagating backwards
ray1 = rtf.ray([0,0,0],[0,0.02999694,0.99954999])
ray3 = rtf.ray([0,0,0],[0,-0.02999694,0.99954999])
ray2 = rtf.ray([0,0,0],[0,0,1])
ray4 = rtf.ray([0,0.5,0],[0,0.01498836,0.99988767])
surf1 = rtf.SphericalRefraction(33.1,0.03,1,1.5,3)
surf2 = rtf.SphericalRefraction(33.3,-0.03,1.5,1,3)
surf1.propagate_ray(ray1)
surf2.propagate_ray(ray1)
surf1.propagate_ray(ray2)
surf2.propagate_ray(ray2)
surf1.propagate_ray(ray3)
surf2.propagate_ray(ray3)
surf1.propagate_ray(ray4)
surf2.propagate_ray(ray4)
print ray1.k()
print ray2.k()
print ray3.k()
print ray4.k()
# quite parallel (inaccuracies due to rounding error)