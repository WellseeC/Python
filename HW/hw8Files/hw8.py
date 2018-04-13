'''
This program is a Angry Birds simulation.
Birds win if they are alive in the field till end with pigs in the field.
Pigs win if all birds fly out of the field or killed by barriers.
Enjoy.
'''
#IMPORTS
from Bird import *
from Pig import *
from Barrier import *
#MAIN CODE
if __name__ == "__main__":
    #Input documents
    bird=str(input('Enter the name of the bird file => '))
    print(bird)
    pig=str(input('Enter the name of the pig file => '))
    print(pig)
    barrier=str(input('Enter the name of the barrier file => '))
    print(barrier)
    #Empty lists
    bird_l=[]
    birdlist=[]
    pig_l=[]
    piglist=[]
    barrier_l=[]
    barrierlist=[]
    #Part of programe deal with the information in the file
    for line in open(bird):
        line=line.strip().split('|')
        bird_l.append(line)    
    for line in open(pig):
        line=line.strip().split('|')
        pig_l.append(line)
    for line in open(barrier):
        line=line.strip().split('|')
        barrier_l.append(line)
    print('')
    #Part of programme introduce how many birds, pigs and barriers in the game and their locations
    print('There are {} birds:'.format(len(bird_l)))
    for i in range(len(bird_l)):
        print('    {}: ({},{})'.format(bird_l[i][0],float(bird_l[i][2]),float(bird_l[i][3])))
        birdlist.append(Bird(bird_l[i][0],bird_l[i][1],bird_l[i][2],bird_l[i][3],bird_l[i][4],bird_l[i][5],bird_l[i][6]))
    print('')
    print('There are {} pigs:'.format(len(pig_l)))
    for i in range(len(pig_l)):
        print('    {}: ({},{})'.format(pig_l[i][0],float(pig_l[i][1]),float(pig_l[i][2])))
        piglist.append(Pig(pig_l[i][0],pig_l[i][1],pig_l[i][2],pig_l[i][3]))
    print('')
    print('There are {} barriers:'.format(len(barrier_l)))
    for i in range(len(barrier_l)):
        print('    {}: ({},{})'.format(barrier_l[i][0],float(barrier_l[i][2]),float(barrier_l[i][3])))
        barrierlist.append(Barrier(barrier_l[i][0],barrier_l[i][1],barrier_l[i][2],barrier_l[i][3],barrier_l[i][4]))
    print('')
    n=0
    for i in range(len(birdlist)):
        print('Time {}: {} starts at ({},{})'.format(n,bird_l[i][0],float(bird_l[i][2]),float(bird_l[i][3])))
        #Birds will fly if their speeds are greater then 6
        while birdlist[i].speed()>=6:
            n+=1
            birdlist[i].common()
            #Birts will fly if they are still in the field (counting includes their radius)
            if birdlist[i].x+birdlist[i].radius>1000 or birdlist[i].x-birdlist[i].radius<0 or birdlist[i].y+birdlist[i].radius>1000 or birdlist[i].y-birdlist[i].radius<0:
                print('Time {}: {} at ({},{}) has left the game'.format(n,birdlist[i].name,birdlist[i].x,birdlist[i].y))
                break
            for j in range(len(piglist)):
                for k in range(len(barrierlist)):
                    if ((birdlist[i].x-piglist[j].x)**2+(birdlist[i].y-piglist[j].y)**2)>(birdlist[i].radius+piglist[j].radius)**2 or ((birdlist[i].x-barrierlist[k].x)**2+(birdlist[i].y-barrierlist[k].y)**2)>(birdlist[i].radius+barrierlist[k].radius)**2:
                        continue
                    else:
                        #Part of programme explain the situation when birds have collisions with pigs
                        if ((birdlist[i].x-piglist[j].x)**2+(birdlist[i].y-piglist[j].y)**2)<=(birdlist[i].radius+piglist[j].radius)**2:
                            birdlist[i].c_pig()
                            print('Time {}: {} at ({},{}) pops {}'.format(n,birdlist[i].name,birdlist[i].x,birdlist[i].y,piglist[j].name))
                            print('Time {}: {} at ({},{}) has (dx, dy) = ({},{})'.format(n,birdlist[i].name,birdlist[i].x,birdlist[i].y,birdlist[i].dx,birdlist[i].dy))
                            piglist.romove(piglist[j])
                            #No more pigs in the game,birds win
                            if len(piglist)==0:
                                print('Time {}: All pigs are popped. The birds win!'.format(n))
                        #Part of programme explain the situation when birds have collisions with barriers
                        elif ((birdlist[i].x-barrierlist[k].x)**2+(birdlist[i].y-barrierlist[k].y)**2)<=(birdlist[i].radius+barrierlist[k].radius)**2:
                            birdlist[i].c_barrier()
                            print('Time {}: {} at ({},{}) hits {}, Strength {}'.format(n,birdlist[i].name,birdlist[i].x,birdlist[i].y,barrierlist[k].name,barrierlist[k].strength))
                            print('Time {}: {} at ({},{}) with speed 0.0 stops'.format(n,birdlist[i].name,birdlist[i].x,birdlist[i].y))
                            barrierlist[k].c_bird(birdlist[i])
                            if barrierlist[k].strength==0.0:
                                print('Time {}: {} crumbles'.format(n,barrierlist[k].name))
                                barrierlist.remove(barrierlist[k])
                                break
    #When all the birds fly out of the field or died, pigs win and print the names of remaining pigs
    print('Time {}: No more birds. The pigs win!'.format(n))
    print('Remaining pigs:')
    for i in range(len(piglist)):
        print(piglist[i].name)
                        
                            