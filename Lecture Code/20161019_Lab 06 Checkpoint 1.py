bd = [ [ '1', '.', '.', '.', '2', '.', '.', '3', '7'],
       [ '.', '6', '.', '.', '.', '5', '1', '4', '.'],
       [ '.', '5', '.', '.', '.', '.', '.', '2', '9'],
       [ '.', '.', '.', '9', '.', '.', '4', '.', '.'],
       [ '.', '.', '4', '1', '.', '3', '7', '.', '.'],
       [ '.', '.', '1', '.', '.', '4', '.', '.', '.'],
       [ '4', '3', '.', '.', '.', '.', '.', '1', '.'],
       [ '.', '1', '7', '5', '.', '.', '.', '8', '.'],
       [ '2', '8', '.', '.', '4', '.', '.', '.', '6'] ]

print('-'*25)
line = '| '
for x in range(9):
    for y in range(9):
        line += str(bd[x][y])+' '
        if y == 2 or y==5 or y ==8:
            line+='| '
    if x<9:
        line+='\n'
    if x == 2 or x == 5 or x == 8:
        line+='-'*25+'\n'
    if x<8:
        line+='| ' 
print(line)