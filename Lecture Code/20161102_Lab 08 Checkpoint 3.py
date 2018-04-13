def get_words(line):
    words=set()
    line=line.split('|')
    word=line[1].replace(',',' ').replace('.',' ').replace('\"',' ').replace('(',' ').replace(')',' ').split(' ')
    for w in word:
        if len(w)>=4 and w.isalpha()==True:
            words.add(w.lower())
    return [line[0],words]
f1=input('Enter a file name => ')
f1=open(f1,encoding = "ISO-8859-1")
f2=open('allclubs.txt',encoding = "ISO-8859-1")
club=[]
line=f1.readline()
name1=get_words(line)[0]
set1=get_words(line)[1]
for line in f2:
    name2=get_words(line)[0]
    set2=get_words(line)[1]
    same=set1.intersection(set2)
    n=0
    for word in same:
        n+=1
    club_info=(n,name2)
    club.append(club_info)
club.sort(reverse=True)
club.pop(0)
i=0
while i < 5:
    print(club[i][1])
    i+=1
