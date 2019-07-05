import raytracerfinal as rtf
import numpy as np

surf = rtf.SphericalRefraction(-1./0.3, 0.3, 0.1, 0.3, 20.)

# Propagation parallel to normal (angle of incidence = 0)
print surf.refract(1,1.5,[0,0,1], [0,0,1])

# Propagation parallel to surface (angle of incidence = pi/2)
k2 = surf.refract(1,1.5,[0,1,0], [0,0,1])
print k2
print np.arccos(np.dot(k2, np.array([0,0,1])))*180/np.pi # find the angle between k2 and n

# travelling towards optically less dense medium with angle of incidence > 
# critical angle, should yield no refracted direction
print surf.refract(1.5,1,np.array([0,1,0.745]),[0,0,1])

# online example, see http://www.starkeffects.com/snells-law-vector.shtml
print surf.refract(1,1.5,np.array([1./np.sqrt(2),0,1./np.sqrt(2)]),np.array([0,0,1]))