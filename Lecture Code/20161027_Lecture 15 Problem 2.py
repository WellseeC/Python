fname = input('Data file name: ')
print(fname)
p = input('Prefix: ')
print(p)
f=open(fname)
k=set()
i=0
for x in f:
    a = x.strip().split('|')
    l = a[0].split(',')[0]
    k.add(l)
for y in list(k):
    if y.startswith(p):
        i+=1
n=len(k)
print(n,'last names')
print(i,'start with',p)