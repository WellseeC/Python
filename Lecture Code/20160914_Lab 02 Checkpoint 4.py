first_name = input('Please enter your first name: ')
print(first_name)
last_name = input('Please enter your last name: ')
print(last_name)
print()
n1 = 6
n2 = len(first_name)
n3 = len(last_name)
n4 = max(n1,n2,n3)
print('*'*(n4+7))
print('*'*2,'Hello,'+' '*(n4-4)+'*'*2)
print('*'*2,first_name+' '*(n4+2-n2)+'*'*2)
print('*'*2,last_name+'!'+' '*(n4-n3+1)+'*'*2)
print('*'*(n4+7))