def get_words(line):
    words=set()
    line=line.split('|')
    word=line[1].replace(',',' ').replace('.',' ').replace('\"',' ').replace('(',' ').replace(')',' ').split(' ')
    for w in word:
        if len(w)>=4 and w.isalpha()==True:
            words.add(w.lower())
    return words

f=input('Enter a file name => ')
x=set()
for line in open(f):
    x=x.union(get_words(line))
print(x)