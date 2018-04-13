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

parse_line('         Here is some spaces 12/32/4')