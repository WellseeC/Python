imdb_file = input("Enter the name of the IMDB file ==> ").strip()
print(imdb_file)
counts = dict()
for line in open(imdb_file, encoding = "ISO-8859-1"):
    words = line.strip().split('|')
    name = words[0].strip()
    if name in counts:
        counts[name] += 1
    else:
        counts[name] = 1
i=0
n=list(counts.keys())
for name in n:
    if counts[name]==1:
            i+=1
    if counts[name]>counts[n[0]]:
        n[0]=name
    
print("{} appears most often: {} times".format(n[0], counts[n[0]]))
print('{} people appear once'.format(i))