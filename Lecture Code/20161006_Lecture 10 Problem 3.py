co2_levels = [ 320.03, 322.16, 328.07, 333.91, 341.47, 348.92, 357.29, 363.77, 371.51, 382.47, 392.95 ]
ave = sum(co2_levels)/len(co2_levels)
b=[]
for n in co2_levels:
    if n>ave:
        b.append(n)
print('Average:',round(ave,2))
print('Num above average:',len(b))