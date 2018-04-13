def parse_line(x):
    y=x.count('/')
    if y < 3:
        return print(None)
    else:
        x=x.split('/')
        a=str(x[-3])
        b=str(x[-2])
        c=str(x[-1])
        if a.isdigit() is False or b.isdigit() is False or c.isdigit() is False:
            return print(None)
        else:
            x.remove(c)
            x.remove(b)
            x.remove(a)
            x='/'.join(x)
            return print((int(a),int(b),int(c),x))

def get_line(fname,parno,lineno):
    f=str(fname)+'.txt'
    f=open(f)
    line= f.read()
    l=[]
    l=line.split('\n')
    a=[]
    b=[]
    for i in range(len(l)):
        if l[i] != '':
            b.append(l[i])
        else:
            a.append(b)
            b=[]
        if i == len(l):
            break
    for j in a:
        if j == []:
            a.remove(j)
    if parno > len(a) or lineno > len(a[parno-1]):
        return None
    return a[parno-1][lineno-1]

fname=int(input('Please enter the file number ==> '))
parno=int(input('Please enter the paragraph number ==> '))
lineno=int(input('Please enter the line number ==> '))
get_line(fname,parno,lineno)