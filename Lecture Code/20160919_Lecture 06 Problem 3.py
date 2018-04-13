x = float(input('Enter the first number: '))
print(x)
y = float(input('Enter the second number: '))
print(y)
z = round((x+y)/2,2)
if x>10 and y>10:
    print('Both are above 10.')
elif x<=10 and y<=10:
    print('Both are below 10.')
print('Average is',z)