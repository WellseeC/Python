f=input('Enter the name of the IMDB file ==> ')
print(f)
f=open(f,encoding='ISO-8859-1')
c=dict()
for line in f:
    words=line.strip().split('|')
    name1=words[1].strip()
    name0=words[0].strip()
    if name1 in c:
        c[name1].add(name0)
    else:
        c[name1]=set([name0])
l=list(c.keys())
n=0
counts=0
name=''
for i in l:
    x=list(c[i])
    t=0
    for j in x:
        t+=1
    if n<t:
        n=t
        name=i
for i in l:
    x=list(c[i])
    t=0
    for j in x:
        t+=1
    if t==1:
        counts+=1
print(n)
print(name)
print(counts)