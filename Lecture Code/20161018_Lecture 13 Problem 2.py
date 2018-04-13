a = input('Enter the scores file: ')
print(a)
b = input('Enter the output file: ')
print(b)
x=[]
for i in open(a):
    x.append(int(i))
x.sort()
y=open(b,'w')
for n in range(len(x)):
    scored='{}: {}\n'.format(n,x[n])
    y.write(scored)
y.close()