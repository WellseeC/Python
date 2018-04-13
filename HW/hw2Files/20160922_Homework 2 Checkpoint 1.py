import math
from math import pi
def volume_sphere(radius):
    o_needed = round(pi*radius**3*4/3*0.21*0.41*300,3)
    print('Oxygen needed for the trip is {0:.3f}m^3.'.format(o_needed))
    return volume_sphere
def volume_cylinder(radius, height):
    v_cylinder = round(pi*radius**2*height*210,3)
    print('Each cylinder holds {0:.3f}m^3 at 3000 psi.'.format(v_cylinder))
    return volume_cylinder

r_capsule = float(input('Radius of capsule (m) ==> '))
print(r_capsule)
r_oreserovir = float(input('Radius of oxygen reservoir (m) ==> '))
print(r_oreserovir)
h_oreserovir = float(input('Height of oxygen reservoir (m) ==> '))
print(h_oreserovir)
print()

volume_sphere = volume_sphere(r_capsule)
volume_cylinder = volume_cylinder(r_oreserovir,h_oreserovir)
n_otanks = math.ceil((pi*r_capsule**3*4/3*0.21*0.41*300)/(pi*r_oreserovir**2*h_oreserovir*210))
print('The trip will require',n_otanks,'reservoir tanks.')