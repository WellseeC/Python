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
print('*'*2+' '*int(round(n4-3+0.5)/2)+'Hello,'+' '*int(round(n4-4+0.5)/2)+'*'*2)
print('*'*2+' '*int(round(n4+2-n2+0.5)/2)+first_name+' '*int(round(n4+3-n2+0.5)/2)+'*'*2)
print('*'*2+' '*int(round(n4-n3+1+0.5)/2)+last_name+'!'+' '*int(round(n4-n3+2+0.5)/2)+'*'*2)
print('*'*(n4+7))