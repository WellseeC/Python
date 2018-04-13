L=[]
n=1
i=-1
while n!=0:
    n=int(input('Enter a value (0 to end): '))
    print(n)
    L.append(n)
    i+=1
L.pop(i)
print('Min:',min(L))
print('Max:',max(L))
print('Avg:',round(sum(L)/i,1))