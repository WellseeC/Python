def bpop_next(bpop,fpop):
    bpop_next = int((10*bpop)/(1+0.1*bpop) - 0.05*bpop*fpop)
    return max(bpop_next,0)
def fpop_next(bpop,fpop):
    fpop_next = int(0.4 * fpop + 0.02 * fpop * bpop)
    return max(fpop_next,0)
bpop=int(input('Number of bunnies ==> '))
print(bpop)
fpop=int(input('Number of foxes ==> '))
print(fpop)
print('Year 1:',bpop,fpop)
b2=bpop_next(bpop,fpop)
f2=fpop_next(bpop,fpop)
print('Year 2:',b2,f2)
bpop=bpop_next(b2,f2)
fpop=fpop_next(b2,f2)
print('Year 3:',bpop,fpop)
b2=bpop_next(bpop,fpop)
f2=fpop_next(bpop,fpop)
print('Year 4:',b2,f2)
bpop=bpop_next(b2,f2)
fpop=fpop_next(b2,f2)
print('Year 5:',bpop,fpop)