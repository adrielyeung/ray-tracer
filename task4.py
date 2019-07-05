import raytracerfinal as rtf
import numpy as np

# 1D case
newray = rtf.ray([0,0,-10-1./0.3],[0,0,1]) # distance = 10 away from lens
surf = rtf.SphericalRefraction(-1./0.3, 0.3, 0.1, 0.3, 20.) # centred at origin
print surf.intercept(newray)

# 2D case
newray2 = rtf.ray([0,-9,-10-1./0.3],[0,1,1]) # should hit the surface a bit higher than the z-axis
print surf.intercept(newray2)
print np.linalg.norm(surf.intercept(newray2))