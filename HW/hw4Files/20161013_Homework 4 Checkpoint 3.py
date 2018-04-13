import hw4_util
def print_pokemon():#function for printing pokemons and loctions in the field
    print('Current pokemon:')
    for i in range(len(pok)):
        print('    ',pok[i],'at',loc[i])
            
def pokemon(command):#function for user giveing direction command
    if command == 'n':
        position[1]-=1
        if position[1] < 0:
            position[1] = 0
    elif command == 's':
        position[1]+=1
        if position[1] > 10:
            position[1] = 10
    elif command == 'w':
        position[0]-=1
        if position[0]<0:
            position[0]=0
    elif command == 'e':
        position[0]+=1
        if position[0]>10:
            position[0]=10
    print('Currently at ('+str(position[0])+',',str(position[1])+')')

pok,loc = hw4_util.read_pokemon()
position=[5,5]
p=(5,5)
i=0
print_pokemon()
print()

while i!=99999:#while loop for the programme running over and over again till user enter end
    command = str(input('N,S,E,W to move, \'print\' to list, or \'end\' to stop ==> '))
    print(command)
    command = command.lower()
    if command == 'n' or command == 's' or command == 'w' or command == 'e':#the smae treatment for users if they enter n,s,w,e four directions
        pokemon(command)
        p=(position[0],position[1])
        i+=1
        if p in loc:
            r=loc.index(p)
            loc.pop(r)
            cap=pok.pop(r)
            print('You capture a',cap,'on turn',i-1)
    elif command == 'print':#call print_pokemon function right here when user what to know the what's the pokemons left and their location
        print_pokemon()
        print()
        print('Currently at ('+str(position[0])+',',str(position[1])+')')
        i+=1
    elif command == 'end':#programme end when user enter end
        i=99999
    else:
        print('Currently at ('+str(position[0])+',',str(position[1])+')')