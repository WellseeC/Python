from math import pi
r1=5
r2=32
a1=1
Area1= pi*r1**2
a2= pi*pow(r2,2)
Area2=round(a2,2)
F='Area {0:.0f} = {1:.2f}'.format(a1,Area1)
print(F)
print('Area 2 =', Area2)