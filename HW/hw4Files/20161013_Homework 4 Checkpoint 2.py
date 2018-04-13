import hw4_util
c1 = input('Enter the first area to check => ')
print(c1)
d1 = hw4_util.read_deaths(c1)#To check the data of the first city
if d1 == []:#To check if c1(city1) is valid or not
    print(c1, 'is an invalid name')
else:
    c2 = input('Enter the second area to check => ')
    print(c2)
    d2 = hw4_util.read_deaths(c2)# To check the data of the second city
    if d2 == []:#To check if c2(city2) is valid or not
        print(c2, 'is an invalid name')
    else:
        i = 10
        t = ''#creat a new str t(trend)
        while i >= 0:
            dif = d1[i] - d2[i]#get the difference of data between c1 and c2 in the same year
            i-=1
            if dif >= 50:
                t += '-'
            elif dif < -50:
                t += '+'
            else:
                t += '='
        print('')
        print('       2013   2003')
        print('Trend:',t)
        print('')
        np = t.count('+')
        nn = t.count('-')
        if np > nn:#check which city people would prefer
            print('I would rather live in',c1,'than',c2)
        elif nn > np:
            print('I would rather live in',c2,'than',c1)
        else:
            print(c1,'and',c2,'are the same')