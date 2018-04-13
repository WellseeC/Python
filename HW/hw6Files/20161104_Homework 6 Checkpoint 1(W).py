'''
This program is going to see how many steps the user will use to find a villain in a chain from of the top ten most popular villains.
'''
def read_file():
    for line in f:
        x=line.split('\t')
        y=x[7].strip().lower().split(',')
        set_of_stories = set()
        for i in y:
            set_of_stories.add(i.strip())
        n=len(set_of_stories)
        a.append([n,x[0].strip(),set_of_stories])
        
def top_10(b):
    for s in a:
        b.append(s)
        if len(b)==11:
            b.sort(reverse=True)
            b.pop()
    print('''1. {}
2. {}
3. {}
4. {}
5. {}
6. {}
7. {}
8. {}
9. {}
10. {}'''.format(b[0][1],b[1][1],b[2][1],b[3][1],b[4][1],b[5][1],b[6][1],b[7][1],b[8][1],b[9][1],))
    
def print_common(b,c,n):
    if len(b[int(sel)-1][2])==1:
        print('{} appeared in {} story and overlapped with:'.format(b[int(sel)-1][1],len(b[int(sel)-1][2])))
    else:
        print('{} appeared in {} stories and overlapped with:'.format(b[int(sel)-1][1],len(b[int(sel)-1][2])))
    print()
    for s in c:
        print('{}. {}'.format(n,s[1]))
        n+=1      
if __name__ == "__main__":
    a=[]
    b=[]
    c=[]
    k=0
    n=1
    i=1
    v=input('Who are you trying to reach? ')
    print(v)
    print()
    f=open('DrWhoVillains.tsv')
    read_file()
    top_10(b)
    sel=input('Enter a selection => ')
    print(sel)
    print()
    while k != 100:
        if sel.isdigit() == False:
            b=[]
            top_10(b)
            sel = input('Enter a selection => ')
            print(sel)
            print()
        elif sel.isdigit():
            if int(sel) not in range(1,11):
                b=[]
                top_10(b)
                sel = input('Enter a selection => ')
                print(sel)
                print()
            else:
                k=100
    if b[int(sel)-1][1]==v.title():
        print('''You reached the villain {} in {} steps.
Have a nice day.'''.format(v.title(),i))
    else:
        for s in a:
            common = b[int(sel)-1][2] & s[2]
            z=len(common)
            if z!=0 and s[2] != b[int(sel)-1][2]:
                c.append(s)
        c.sort(reverse=True)
        print_common(b,c,n)
        sel=input('Enter a selection => ')
        print(sel)
        print()
        while k != 0:
            if sel.isdigit()==False:
                d=[]
                n=1
                print_common(c,d,n)
                sel=input('Enter a selection => ')
                print(sel)
                print()
            elif sel.isdigit():
                if int(sel) not in range(1,n+1):
                    d=[]
                    n=1
                    print_common(c,d,n)
                    sel=input('Enter a selection => ')
                    print(sel)
                    print()
                else:
                    k=0
        i+=1
        if c[int(sel)-1][1] == v.title():
            print('''You reached the villain {} in {} steps.
Have a nice day.'''.dormat(v.title(),i))
        else:
            for s in a:
                common=c[int(sel)-1][2] & s[2]
                z=len(common)
                if z!=0 and s[2] !=c[int(sel)-1][2]:
                    d=[]
                    d.append(s)
            d.sort(reverse=True)
            print_common(c,d,n)
            sel=input('Enter a selection => ')
            print(sel)
            print()
            while k!=100:
                if sel.isdigit()==False:
                    c=[]
                    n=1
                    print_common(d,c,n)
                    sel=input('Enter a selection=>')
                    print(sel)
                    print()
                elif sel.isdight():
                    if int(sel) not in range(1,n+1):
                        c=[]
                        n=1
                        print_common(d,c,n)
                        sel=input('Enter a selection=>')
                        print(sel)
                        print()
                    else:
                        k=100
            i+=1
            if d[int(sel)-1][1]==v.title():
                print('''You reached the villain {} in {} steps.
Have a nice day.'''.format(v.title(),i))
            else:
                for s in a:
                    common = d[int(sel)-1][2] & s[2]
                    z=len(common)
                    if z!=0 and s[2] != d[int(sel)-1][2]:
                        c=[]
                        c.append(s)
                c.sort(reverse=True)
                print_common(d,c,n)
                sel=input('Enter a selection => ')
                print(sel)
                print()
                while k != 0:
                    if sel.isdigit()==False:
                        d=[]
                        n=1
                        print_common(c,d,n)
                        sel=input('Enter a selection => ')
                        print(sel)
                        print()
                    elif sel.isdigit():
                        if int(sel) not in range(1,n+1):
                            d=[]
                            n=1
                            print_common(c,d,n)
                            sel=input('Enter a selection => ')
                            print(sel)
                            print()
                        else:
                            k=0
                i+=1
                if c[int(sel)-1][1] == v.title():
                    print('''You reached the villain {} in {} steps.
Have a nice day.'''.dormat(v.title(),i))
                else:
                    for s in a:
                        common=c[int(sel)-1][2] & s[2]
                        z=len(common)
                        if z!=0 and s[2] !=c[int(sel)-1][2]:
                            d=[]
                            d.append(s)
                    d.sort(reverse=True)
                    print_common(c,d,n)
                    sel=input('Enter a selection => ')
                    print(sel)
                    print()
                    while k!=100:
                        if sel.isdigit()==False:
                            c=[]
                            n=1
                            print_common(d,c,n)
                            sel=input('Enter a selection=>')
                            print(sel)
                            print()
                        elif sel.isdight():
                            if int(sel) not in range(1,n+1):
                                c=[]
                                n=1
                                print_common(d,c,n)
                                sel=input('Enter a selection=>')
                                print(sel)
                                print()
                            else:
                                k=100
                    i+=1
                    if d[int(sel)-1][1]==v.title():
                        print('''You reached the villain {} in {} steps.
Have a nice day.'''.format(v.title(),i))