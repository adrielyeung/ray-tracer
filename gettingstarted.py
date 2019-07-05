# IPython log file

import pylab as pl
import raytracerfinal as rtf
testray = rtf.ray([0,0.1,0],[0,0,1])
surf1 = rtf.SphericalRefraction(20,0.03,1,1.5,10)
surf2 = rtf.SphericalRefraction(60,0,1.5,1.5,20)
out = rtf.OutputPlane(250)
# determination of paraxial focus
surf1.propagate_ray(testray)
surf2.propagate_ray(testray)
out.propagate_ray(testray)
get_ipython().magic(u'matplotlib qt')
pl.plot(testray.z(),testray.y())
pl.grid()
pl.xlabel("z")
pl.ylabel("y")
# paraxial focus at z ~ 120
out = rtf.OutputPlane(120)
raybun1 = rtf.raybun(5, 3, 6)
raybun1.propagate_raybun(surf1, surf2, out)
raybun2 = rtf.raybun(5,3,6,-2,[2,0,20])
raybun2.propagate_raybun(surf1, surf2, out)
pl.figure()
# path of ray plot
rtf.plotxz(raybun1, "singlet f = 100")
rtf.plotxz(raybun2, "singlet f = 100")
# spot diagram plot
pl.figure()
pl.subplot(2,2,1)
rtf.plotxy(raybun1)
pl.axis([-4,4,-3,3])
pl.subplot(2,2,2)
rtf.plotxy(raybun2)
pl.axis([-6,2,-3,3])
pl.subplot(2,2,3)
rtf.plotxy(raybun1, False)
pl.subplot(2,2,4)
rtf.plotxy(raybun2, False)
# find rms values for various beam radii
pl.figure()
rtf.plotrms(surf1, surf2, out, 100)
