#trick
print('Enter a 5 digit number whose first and third digits must differ by at least 2.')
print('The answer will be 1089, if your number is valid')
def dights(v):
    a=v//100
    b=a//100+a//10%10*10+a%10*100
    c=max(a,b)-min(a,b)
    d=c//100+c//10%10*10+c%10*100
    e=d+(d//100+d//10%10*10+d%10*100)
    f=v%10*10000+(v%100-v%10)*100+b
    print('Here is the computation:')
    print(value,'reversed is',f)
    print(max(a,b),'-',min(a,b),'=',c)
    print(c,'+',d,'=',e)
    print('You see, I told you.')
    return dights
value = int(input('Enter a value ==> '))
print(value)
print()
value=dights(value)

#reverse 3
def reverse3(v):
    r3=v//100+v//10%10*10+v%10*100
    return r3
x = int(input())   #Submitty will report my mistake if I enter something in the brackets of input   
print(x)
re3=reverse3(x)
print(re3)

#reverse 5
def reverse5(v):
    r5=v%10*10000+(v%100-v%10)*100+v//10000+v//100//10%10*10+v//100%10*100
    return r5
y = int(input())
print(y)
re5=reverse5(y)
print(re5)