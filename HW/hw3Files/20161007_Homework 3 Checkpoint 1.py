'''Popular Baby Names'''
#This programme is used to test how the popular baby names changed in the range of 1880 to 2014.
import read_names

#Function find_names is setted by using variables y(year),g(gender) and n(name);write this as a function because it will be used multiple times in the later codes
def find_names(y,g,n):
    (names,counts) = read_names.top_in_year(y,g)
    if not n in names:
        print('{:7d}: Not in the top 250'.format(y))
    else:
        r = names.index(n)
        x = counts[r]
        a = x/counts[0]*100
        b = x/sum(counts)*100
        print('{:7d}: {:3d} {:5d} {:7.3f} {:7.3f}'.format(y,r+1,x,a,b))
        
read_names.read_from_file('top_names_1880_to_2014.txt')

#Users enters a year they want to check
y = int(input('Enter the year to check => '))
print(y)

#When the year is out of the range of data, the programme will stop after print 'Year must be at least 1880 and at most 2014'
if y<1880 or y>2014:
    print('Year must be at least 1880 and at most 2014')
#If the year is in the range, the progamme will show the year tested(including recent years with the gap of 5),the rank, the count, the percentage of the count relative to the count of the top ranked name, and the percentage of the name relative to the sum of all the name sounts in the top 250.
else:
    f_name = input('Enter a female name => ')
    print(f_name)
    print('Data about female names')
    print(f_name+':')
    if y-10>=1880:
        find_names(y-10,'f',f_name)
    if y-5>=1880:
        find_names(y-5,'f',f_name)
    find_names(y,'f',f_name)
    if y+5<=2014:
        find_names(y+5,'f',f_name)
    if y+10<=2014:
        find_names(y+10,'f',f_name)
    print()
    m_name = input('Enter a male name => ')
    print(m_name)
    print('Data about male names')
    print(m_name+':') 
    if y-10>=1880:
        find_names(y-10,'m',m_name)
    if y-5>=1880:
        find_names(y-5,'m',m_name)
    find_names(y,'m',m_name)
    if y+5<=2014:
        find_names(y+5,'m',m_name)
    if y+10<=2014:
        find_names(y+10,'m',m_name)
#The programme can test one female name and one male name around a single fiven year every time.