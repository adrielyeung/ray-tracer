import raytracerfinal as rtf
import pylab as pl

surf1 = rtf.SphericalRefraction(19.9,0.03,1,1.5,3)
surf2 = rtf.SphericalRefraction(20.1,-0.03,1.5,1,3)
ray1 = rtf.ray([0,1,0],[0,0,1])
ray2 = rtf.ray([0,0,0],[0,0,1])
ray3 = rtf.ray([0,-1,0],[0,0,1])
out = rtf.OutputPlane(53.2)
surf1.propagate_ray(ray1)
surf2.propagate_ray(ray1)
out.propagate_ray(ray1)
surf1.propagate_ray(ray2)
surf2.propagate_ray(ray2)
out.propagate_ray(ray2)
surf1.propagate_ray(ray3)
surf2.propagate_ray(ray3)
out.propagate_ray(ray3)
print ray1.p()
print ray1.vertices()
print ray1.k()
# 4 points obtained as expected

# try plotting path of rays, see p. 39 for diagram
get_ipython().magic(u'matplotlib qt')
pl.figure()
pl.plot(ray1.z(), ray1.y())
pl.plot(ray2.z(), ray2.y())
pl.plot(ray3.z(), ray3.y())
pl.xlabel("z")
pl.ylabel("y")
pl.grid()

# paraxial focus
testray = rtf.ray([0,0.1,0],[0,0,1])
surf1.propagate_ray(testray)
surf2.propagate_ray(testray)
out.propagate_ray(testray)
pl.figure()
pl.plot(testray.z(), testray.y())
pl.xlabel("z")
pl.ylabel("y")
pl.grid()
# diagram on p. 40

# using ray bundle to obtain spot diagram
surf2 = rtf.SphericalRefraction(20.5,-0.03,1.5,1,3.1)
surf1 = rtf.SphericalRefraction(19.5,0.03,1,1.5,3.1)
out = rtf.OutputPlane(53.67)	 # found by using test ray
raybun1 = rtf.raybun(5, 3, 6)
raybun1.propagate_raybun(surf1, surf2, out)
pl.figure()
rtf.plotxy(raybun1)
pl.figure()
rtf.plotxy(raybun1, False)
# see diagrams on p. 41

# using ray bundle not parallel to optical axis
pl.figure()
raybun2 = rtf.raybun(5,3,6,-2,[2,0,20])
rtf.plotxy(raybun2)
surf1 = rtf.SphericalRefraction(19.5,0.03,1,1.5,3.1)
surf2 = rtf.SphericalRefraction(20.5,-0.03,1.5,1,3.1)
out = rtf.OutputPlane(53.67)
raybun2.propagate_raybun(surf1, surf2, out)
pl.figure()
rtf.plotxy(raybun2, False)
# see p. 42

# now tried plotting ray paths in the x-z plane
pl.figure()
rtf.plotxz(raybun1, "convex lens f = 33.7")
rtf.plotxz(raybun2, "convex lens f = 33.7")
# see p. 43

# finding rms value for raybun1
print rtf.rms(raybun1)
