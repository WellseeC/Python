'''Legos'''
#This programme is used to test how many pieces of required lego can be made within limited lego materials
import hw3_util

#Two functions have been used. pl(a) means print of legos and it is written in nl(a),which means number of legos, to simplify the program.
def nl(a):
#n11 means number of 1x1 pieces, n21 means number of 2x1 pieces, n22 means number of 2x2 pieces, n24 means number of 2x4 pieces and t means the total number of pieces has been used.
    def pl(a):
        print('''I can make {} {} pieces:
     {} pieces of {} using 2x4 pieces.
     {} pieces of {} using 2x2 pieces.
     {} pieces of {} using 2x1 pieces.
     {} pieces of {} using 1x1 pieces.'''.format(t,a,n24,a,n22,a,n21,a,n11,a))
        
#Using if and elif to give every possible result of input.
    if a == '1x1':
        n11=legos.count('1x1')
        n21=0
        n22=0
        n24=0
        t = n11+n21+n22+n24
        pl(a)
    elif a =='2x1':
        n11=legos.count('1x1')//2
        n21=legos.count('2x1')
        n22=0
        n24=0
        t = n11+n21+n22+n24
        pl(a)
    elif a == '2x2':
        n11=legos.count('1x1')//4
        n21=legos.count('2x1')//2
        n22=legos.count('2x2')
        n24=0
        t = n11+n21+n22+n24
        pl(a)
    elif a == '2x4':
        n11=legos.count('1x1')//8
        n21=legos.count('2x1')//4
        n22=legos.count('2x2')//2
        n24=legos.count('2x4')
        t = n11+n21+n22+n24
        pl(a)
    else:
        print('Illegal lego')

legos = hw3_util.read_legos('legos.txt')

#Using a as variable of input.
a = input('What type of lego do you need? ==> ')
print(a)
print()
#Call the function
nl(a)