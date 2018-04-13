from math import pi
d_Jupiter = 88846
avds_Jupiter = 483632000
d_Earth = 7926
avds_Earth = 92957100
d_Sun = 864938
s_light = 186000
ratio_SJ = (d_Sun/2)/(d_Jupiter/2)
ratio_SE = (d_Sun/2)/(d_Earth/2)
ratio_JE = (d_Jupiter/2)/(d_Earth/2)
ratioavds_JE = avds_Jupiter/avds_Earth
ratiov_SJ = (4/3*pi*(d_Sun/2)**3)/(4/3*pi*(d_Jupiter/2)**3)
ratiov_SE = (4/3*pi*(d_Sun/2)**3)/(4/3*pi*(d_Earth/2)**3)
ratiov_JE = (4/3*pi*(d_Jupiter/2)**3)/(4/3*pi*(d_Earth/2)**3)
timem_SE = avds_Earth/s_light/60
timem_SJ = avds_Jupiter/s_light/60
print('Sun-to-Jupiter radius ratio:', round(ratio_SJ,2))
print('Sun-to-Earth radius ratio:', round(ratio_SE,2))
print('Jupiter-to-Earth radius ratio:', round(ratio_JE,2),end='\n\n')
print('Jupiter-to-Earth Sun distance ratio:', round(ratioavds_JE,2))
print('Sun-to-Jupiter volume ratio:', round(ratiov_SJ,2))
print('Sun-to-Earth volume ratio:', round(ratiov_SE,2))
print('Jupiter-to-Earth volume ratio:', round(ratiov_JE,2),end='\n\n')
print('Sun to Earth light travel time in minutes:', round(timem_SE,2))
print('Sun to Jupiter light travel time in minutes:', round(timem_SJ,2))