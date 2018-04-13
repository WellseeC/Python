def line(bd):
  print('-'*25)
  line = '| '
  for x in range(9):
    for y in range(9):
        line += str(bd[x][y])+' '
        if y == 2 or y == 5 or y == 8:
              line+='| '
    if x<9:
        line+='\n'
    if x == 2 or x == 5 or x == 8:
        line+='-'*25+'\n'
    if x<8:
        line+='| ' 
  print(line)   
def ok_to_add(x,y,n,bd):
  if n in bd[x]:
      return False
  for i in range(9):
      if n in bd[i][y]:
        return False
  board_3x3 = ''
  if x in range(0,3) and y in range(0,3):
    for x in range(0,3):
      for y in range(0,3):
          board_3x3 += bd[x][y]        
  if x in range(0,3) and y in range(3,6):
    for x in range(0,3):
      for y in range(3,6):
        board_3x3 += bd[x][y]        
  if x in range(0,3) and y in range(6,9):
    for x in range(0,3):
      for y in range(6,9):
        board_3x3 += bd[x][y]       
  if x in range(3,6) and y in range(0,3):
    for x in range(3,6):
      for y in range(0,3):
        board_3x3 += bd[x][y]       
  if x in range(3,6) and y in range(3,6):
    for x in range(3,6): 
      for y in range(3,6):
        board_3x3 += bd[x][y]       
  if x in range(3,6) and y in range(6,9):
    for x in range(3,6):
      for y in range(6,9):
        board_3x3 += bd[x][y]
  if x in range(6,9) and y in range(0,3):
    for x in range(6,9):
      for y in range(0,3):
        board_3x3 += bd[x][y]  
  if x in range(6,9) and y in range(3,6):
    for x in range(6,9):
      for y in range(3,6):
        board_3x3 += bd[x][y]
  if x in range(6,9) and y in range(6,9):
    for x in range(6,9): 
      for y in range(6,9):
        board_3x3 += bd[x][y]
  if n in board_3x3:
    return False         
  return True
                    
x = int(input('Enter a row number: '))
y = int(input('Enter a column number: '))
n = input('Enter a number to be added in: ')
bd = [ [ '1', '.', '.', '.', '2', '.', '.', '3', '7'],
       [ '.', '6', '.', '.', '.', '5', '1', '4', '.'],
       [ '.', '5', '.', '.', '.', '.', '.', '2', '9'],
       [ '.', '.', '.', '9', '.', '.', '4', '.', '.'],
       [ '.', '.', '4', '1', '.', '3', '7', '.', '.'],
       [ '.', '.', '1', '.', '.', '4', '.', '.', '.'],
       [ '4', '3', '.', '.', '.', '.', '.', '1', '.'],
       [ '.', '1', '7', '5', '.', '.', '.', '8', '.'],
       [ '2', '8', '.', '.', '4', '.', '.', '.', '6'] ]
if bd[x][y] == '.':
  if ok_to_add(x,y,n,bd):
    bd[x][y]=n
    line(bd)
  else:
    print('This number cannot be added')
else:
  print ('This number cannot be added...')  