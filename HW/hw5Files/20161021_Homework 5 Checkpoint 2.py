import random #import random for later programmes that can give a random number
def move_trainer(position,bounds,prob): #combine move function and move_trainer function together from Part 1 for Part 2 situation
    x=random.randint(0,3)
    if x == 0:
        position[0]-=1
        if position[0]<0: #to make sure trainer is still in the field
            position[0]=0
    if x == 1:
        position[0]+=1
        if position[0]>bounds[0]: #to make sure trainer is still in the field
            position[0]=bounds[0]       
    if x == 2:
        position[1]+=1
        if position[1]>bounds[1]: #to make sure trainer is still in the field
            position[1]=bounds[1]        
    if x == 3:
        position[1]-=1
        if position[1]<0: #to make sure trainer is still in the field
            position[1]=0    
    if random.random()<prob: #to determine the probability of catch a pokemon
        return position, True
    else:
        return position, False
    
def run_one_simulation(grid,prob): #to get the grid and total pokemon caught in one simulation
    position=[M//2,N//2]
    n=0
    for i in range(250):
        y,result = move_trainer(position,bounds,prob)
        if  result:
            grid[y[0]][y[1]]+=1
            n+=1
    return [grid,n]

def pgrid(grid): #print the grid
    for i in range(M):
        a=''
        for j in range(N):
            a+='{:4d}'.format(grid[i][j])
        print(a)
        
def mins(x): #find the min number of pokemon caught in the grid at a space
    mins = x[0][0]
    for i in x:
        for j in i:
            if j < mins:
                mins = j
    return mins

def maxs(x): #find the max number of pokemon caught in the grid at a space
    maxs = x[0][0]
    for i in x:
        for j in i:
            if j > maxs:
                maxs = j
    return maxs

M = int(input('Enter the integer number of rows => ')) #Enter in rows of field
print(M)
N = int(input('Enter the integer number of cols => ')) #Enter in cols of field
print(N)
P = float(input('Enter the probability of finding a pokemon (<= 1.0) => ')) #Enter in probability of finding a pokemon
print(P)
R = int(input('Enter the number of simulations to run => ')) #Enter the times of simulation user want to have
print(R)
seed_value = 10*M+N
random.seed(seed_value)
bounds = (M-1,N-1) #show how big the field is
position = [M//2,N//2] #initial position of trainer
nlist=[] #empty list for pokemon number
grid=[] #empty list for grid
for i in range(M):
    grid.append([0]*N)
for i in range(R):
    [grid,n]=run_one_simulation(grid,P)
    nlist.append(n)
t=sum(nlist) #total pokemon caught
mins=mins(grid) 
minv=min(nlist) #min number of pokemon caught in a single simulation
minpos=nlist.index(minv)+1 #find the simulation of minv
maxs=maxs(grid)
maxv=max(nlist) #max number of pokemon caught in a single simulation
maxpos=nlist.index(maxv)+1 #find the simulation of maxv
if t == 0: #to avoid the situation that when t as a divisor equals to 0
    maxper=0 #percent of max number of pokemon caught in a space
    minper=0 #percent of min number of pokemon caught in a space
else:
    maxper=maxs*100/t #percent of max number of pokemon caught in a space
    minper=mins*100/t #percent of min number of pokemon caught in a space
print('')
pgrid(grid)
print('')    
if t != 0:
    print('''Total pokemon caught is {}
Minimum pokemon caught was {} in simulation {}
Maximum pokemon caught was {} in simulation {}
Max number of pokemon caught on a space is {} which was {:.2f}% of all pokemon caught
Min number of pokemon caught on a space is {} which was {:.2f}% of all pokemon caught'''.format(t,minv,minpos,maxv,maxpos,maxs,maxper,mins,minper))
    
else:
    print('''Total pokemon caught is {}
Minimum pokemon caught was {} in simulation {}
Maximum pokemon caught was {} in simulation {}
Max number of pokemon caught on a space is 0
Min number of pokemon caught on a space is 0'''.format(t,minv,minpos,maxv,maxpos))