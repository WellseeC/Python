def get_words(line):
    words=set()
    line=line.split('|')
    word=line[1].replace(',',' ').replace('.',' ').replace('\"',' ').replace('(',' ').replace(')',' ').split(' ')
    for w in word:
        if len(w)>=4 and w.isalpha()==True:
            words.add(w.lower())
    return words

f1=input('Enter the first file => ')
f2=input('Enter the second file => ')
x=set()
y=set()
for line in open(f1):
    x=x.union(get_words(line))
for line in open(f2):
    y=y.union(get_words(line))
same=x.intersection(y)
unique1=x-y
unique2=y-x
print('same words',same)
print('unique to {}:'.format(f1),unique1)
print('unique to {}:'.format(f2),unique2)