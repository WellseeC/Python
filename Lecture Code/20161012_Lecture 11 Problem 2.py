hd = int(input('Enter Dale\'s height: '))
print(hd)
he = int(input('Enter Erin\'s height: '))
print(he)
hs = int(input('Enter Sam\'s height: '))
print(hs)
if hd>he and he>hs:
    print('Dale'+'\n'+'Erin'+'\n'+'Sam')
elif hd>hs and hs>he:
    print('Dale'+'\n'+'Sam'+'\n'+'Erin')
elif he>hd and hd>hs:
    print('Erin'+'\n'+'Dale'+'\n'+'Sam')
elif he>hs and hs>hd:
    print('Erin'+'\n'+'Sam'+'\n'+'Dale')
elif hs>hd and hd>he:
    print('Sam'+'\n'+'Dale'+'\n'+'Erin')
else:
    print('Sam'+'\n'+'Erin'+'\n'+'Dale')