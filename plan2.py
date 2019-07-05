# IPython log file

import numpy as np
import pylab as pl
import raytracerfinal as rtf
testray = rtf.ray([0,0.1,0],[0,0,1])
surf1 = rtf.SphericalRefraction(20,0.02,1,1.5168,5.5)
surf2 = rtf.SphericalRefraction(25,0,1.5168,1,5.5)
out = rtf.OutputPlane(75)
# determination of paraxial focus
surf1.propagate_ray(testray)
surf2.propagate_ray(testray)
out.propagate_ray(testray)
get_ipython().magic(u'matplotlib qt')
pl.plot(testray.z(),testray.y())
pl.grid()
pl.xlabel("z")
pl.ylabel("y")
# output plane not far enough, set z = 160
out = rtf.OutputPlane(160)
testray = rtf.ray([0,0.1,0],[0,0,1])
surf1.propagate_ray(testray)
surf2.propagate_ray(testray)
out.propagate_ray(testray)
pl.figure()
pl.plot(testray.z(),testray.y())
pl.grid()
pl.xlabel("z")
pl.ylabel("y")
# paraxial focus at z ~ 118.45
out = rtf.OutputPlane(118.45)
raybun1 = rtf.raybun(5, 5, 6)
raybun1.propagate_raybun(surf1, surf2, out)
pl.figure()
# path of ray plot
rtf.plotxz(raybun1, "planoconvex f = 99.25 mm")
# spot diagram plot
pl.figure()
pl.subplot(2,1,1)
rtf.plotxy(raybun1)
pl.subplot(2,1,2)
rtf.plotxy(raybun1, False)
# find rms values for various beam radii
pl.figure()
rtf.plotrms(surf1, surf2, out, 99.25, np.linspace(2.5e-3, 5, 50))
