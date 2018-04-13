
def fib(n):
    L=[]
    if n==0:
        return 0
    elif n==1:
        return 1
    else:
        i=1
        L=[0,1]
        while i<n:
            L.append(L[i-1]+L[i])
            i+=1
    return L[-1]

if __name__ == "__main__":
    print( fib(0) )
    print( fib(1) )
    print( fib(2) )
    print( fib(5) )
    print( fib(10) )
