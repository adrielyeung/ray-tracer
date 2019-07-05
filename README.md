# ray-tracer
(Project for 2nd Year Computing course in spring 2017)

Optical ray tracing is important in designing optical equipment before production. A simple optical system, lenses, is simulated here, using geometric optics.

Program written in Python 3. This folder contains:
- ```genpolar.py```
  This is the code for generating uniformly distributed radius and angle pairs (written as a separate exercise in the course).
- ```gettingstarted.py```
  This is the code for generating results for the single spherical surface case.
- ```plan1.py```
  This is the code for generating results for planoconvex lens orientation 1, i.e.
  with plane surface facing light source.
- ```plan2.py```
  This is the code for generating results for planoconvex lens orientation 2, i.e.
  with convex surface facing light source.
- ```raytracerfinal.py```
  This is the code that contains all elements involved in the ray tracer, including classes
  ```ray, SphericalRefraction, OutputPlane``` and ```raybun```.
- ```task4.py```
  This is the code for the tests in Task 4: Create a method intercept (```ray```) for your ```SphericalRefraction``` class that calculates the first valid intercept of a ray with the spherical surface. Remember a line can have two intercepts with a sphere — make sure you get the correct intercept for your surface. This should be the first intercept along the forward direction of the ray that lies within the aperture of the surface. Note: you may need to treat the case where the curvature is zero as special case. If there is no valid intercept, then your method should return ```None```.
- ```task5.py```
  This is the code for the tests in Task 5: Write a function to implement Snell’s law of refraction. Your function should take an incident direction and a surface normal (both as unit vectors) and the refractive indices ```n1``` and ```n2``` as parameters. It should return the refracted ray direction (a unit vector). (Hint: the refracted ray should be in the same plane as the incident ray and the surface normal.) If the ray is subject to total internal reflection (i.e., sin $θ_1 > n_2/n_1$) your function should return ```None```.
- ```task7.py```
  This is the code for the tests in Task 7: Test your code. Create a refracting surface and a ray and check ```propagate_ray``` correctly propagates and refracts the ray. Try a range of initial rays to check your refracting object behaves as you expect.
- ```task8.py```
  This is the code for the tests in Task 8: Write a class ```OutputPlane```, that is an ```OpticalElement```. Implement methods ```intercept``` and ```propagate_ray```.
 
Results are detailed in the PDF report.

## Acknowledgements
Credits to Dr. Carl Paterson for designing the project. Also special thanks to my labbie (lab partner :P) Meryl for completing the project with me all along.
