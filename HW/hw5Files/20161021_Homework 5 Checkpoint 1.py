import random #import random for later programmes that can give a random number
def move(position,bounds): #move function for which direction trainer choose to move when a random integer 0~3 is given
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
    
def move_trainer(position,bounds,prob):
    i=1
    nt=0 #total number of pokemon can be caught
    n=0 #number of pokemon caught by trainer after 20 times of movement
    while i<251: #support trainer to move 250 times
        move(position,bounds)
        if random.random()<prob:
            nt+=1
            n+=1
            if i%20==0:
                print('Time step {}: position ({}, {}) pokemon caught since the last report {}'.format(i,position[0],position[1],n))
                n=0 #recount the number of pokemon caught by trainer after 20 times of movement
        else:
            if i%20==0:
                print('Time step {}: position ({}, {}) pokemon caught since the last report {}'.format(i,position[0],position[1],n))
                n=0 #recount the number of pokemon caught by trainer after 20 times of movement
        i+=1
                
    print('After 250 time steps the trainer ended at position ({}, {}) with {} pokemon.'.format(position[0],position[1],nt))
            
        
M = int(input('Enter the integer number of rows => ')) #Enter in rows of field
print(M)
N = int(input('Enter the integer number of cols => ')) #Enter in cols of field
print(N)
P = float(input('Enter the probability of finding a pokemon (<= 1.0) => ')) #Enter in probability of finding a pokemon
print(P)
seed_value = 10*M+N
random.seed(seed_value)
bounds = [M-1,N-1] #show how big the field is
position = [M//2,N//2] #initial position of trainer
move_trainer(position,bounds,P) #Call the function