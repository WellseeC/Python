'''Turtle Moves!'''
#This programme is used for ...... FUN~
#Functions move and turn as required are mean to give instruction of moving and turning around
def move(x,y,direction,amount):
    if direction == 'right':
        x += amount
        if x> 400:
            x = 400
    elif direction == 'left':
        x -= amount
        if x< 0:
            x = 0
    elif direction == 'up':
        y -= amount
        if y< 0:
            y = 0
    elif direction == 'down':
        y += amount
        if y> 400:
            y = 400
    return (x, y)
def turn(direction):
    if direction == 'right':
        return 'up'
    elif direction == 'up':
        return 'left'
    elif direction == 'left':
        return 'down'
    elif direction == 'down':
        return 'left'

#initial values of varaibles are setted
i=0
(x, y) = (200, 200)
direction = 'right'
print('Turtle: {} facing: {}'.format((x, y), direction))
ac = []

#use while loop to 4 times to prevent if the last command is 'sleep'
while i<4:
    c = input('Command (move,jump,turn,sleep) => ')
    print(c)
    ac.append(c)
    if c.lower() == 'move':
        (x, y)=move(x,y,direction,20)
        i+=1
    elif c.lower() == 'jump':
        (x, y)=move(x,y,direction,50)
        i+=1
    elif c.lower() == 'sleep':
        print('Turtle falls asleep.')
        print('Turtle: {} facing: {}'.format((x, y), direction))
        print('Turtle is currently sleeping ... no command this turn.')
        i+=2
    elif c.lower() == 'turn':
        direction=turn(direction)
        i+=1
    else:
        i+=1
    print('Turtle: {} facing: {}'.format((x, y), direction))

#individually use the similar code again to fit the situation if the last command is 'sleep'
c = input('Command (move,jump,turn,sleep) => ')
print(c)
ac.append(c)    
if c.lower() == 'move':
    (x, y)=move(x,y,direction,20)
    i+=1
elif c.lower() == 'jump':
    (x, y)=move(x,y,direction,50)
    i+=1
elif c.lower() == 'sleep':
    print('Turtle falls asleep.')
    i+=2
elif c.lower() == 'turn':
    direction=turn(direction)
    i+=1
else:
    i+=1
print('Turtle: {} facing: {}'.format((x, y), direction))

#print all commands and sorted commands as required
print()
print('All commands entered:',ac)
ac.sort()
print('Sorted commands:',ac)