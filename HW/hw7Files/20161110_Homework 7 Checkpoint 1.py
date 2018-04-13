'''This program reads in a year in the interval 1956 through 2015 and will show the temperature data from Troy,NY in 'Temperatures', 'Precipitation', 'Average temperatures' and 'Temperature histograms' four different aspects.(measured at Hudson River Lock and Dam)'''
#IMPORTS
import json
#FUNCTIONS
#find_year function => create a list of dict of temperature information that belongs to the same year 
def find_year(year):
    for i in data:
        if i['year'] == year:
            y.append(i)
#hl_temperatures function => sort and print highest maximum temperature, lowest minimum temperature and months in a given year            
def hl_temperatures(l):
    x=[]
    y=[]
    for i in l:
        x.append((i['EMXT'],i['month']))
        y.append((i['EMNT'],i['month']))
    x.sort()
    y.sort()
    print('Highest max value => {}: {:.1f}, {}: {:.1f}, {}: {:.1f}'.format(x[-1][1],x[-1][0],x[-2][1],x[-2][0],x[-3][1],x[-3][0]))
    print('Lowest min value => {}: {:.1f}, {}: {:.1f}, {}: {:.1f}'.format(y[0][1],y[0][0],y[1][1],y[1][0],y[2][1],y[2][0]))
#max_temperatures function => sort and print highest number of days with maximum temperature above 90, below 32 and months in a given year
def max_temperatures(l):
    x=[]
    y=[]
    for i in l:
        if i['DT90']!=-9999:
            x.append((i['DT90'],i['month']))
        if i['DX32']!=-9999:
            y.append((i['DX32'],i['month']))
    x.sort()
    y.sort()
    if len(x)>3:
        print('Highest days with max >= 90 => {}: {:.1f}, {}: {:.1f}, {}: {:.1f}'.format(x[-1][1],x[-1][0],x[-2][1],x[-2][0],x[-3][1],x[-3][0]))
    else:
        print('Highest days with max >= 90 => Not enough data')
    if len(y)>3:
        print('Highest days with max <= 32 => {}: {:.1f}, {}: {:.1f}, {}: {:.1f}'.format(y[-1][1],y[-1][0],y[-2][1],y[-2][0],y[-3][1],y[-3][0]))
    else:
        print('Highest days with max <= 32 => Not enough data')
#hlts_precipitation function => sort and print highest total precipitation, lowest total precipitation, highest snow depth, lowest snow depth and months in a given year
def hlts_precipitation(l):
    x=[]
    y=[]
    for i in l:
        if i['TPCP']!=-9999:
            x.append((i['TPCP'],i['month']))
        if i['TSNW']!=-9999:
            y.append((i['TSNW'],i['month']))
    x.sort()
    y.sort()
    if len(x)>3:
        print('Highest total => {}: {:.1f}, {}: {:.1f}, {}: {:.1f}'.format(x[-1][1],x[-1][0],x[-2][1],x[-2][0],x[-3][1],x[-3][0]))
        print('Lowest total => {}: {:.1f}, {}: {:.1f}, {}: {:.1f}'.format(x[0][1],x[0][0],x[1][1],x[1][0],x[2][1],x[2][0]))
    else:
        print('Highest total => Not enough data')
        print('Lowest total => Not enough data')
    if len(y)>3:
        print('Highest snow depth => {}: {:.1f}, {}: {:.1f}, {}: {:.1f}'.format(y[-1][1],y[-1][0],y[-2][1],y[-2][0],y[-3][1],y[-3][0]))
        print('Lowest snow depth => {}: {:.1f}, {}: {:.1f}, {}: {:.1f}'.format(y[0][1],y[0][0],y[1][1],y[1][0],y[2][1],y[2][0]))
    else:
        print('Highest snow depth => Not enough data')
        print('Lowest snow depth => Not enough data')
#ave_temperatures function => calculate and print overall average temperature, average temperature in the first 6 months and average temperature in the last 6 months in a given year
def ave_temperatures(l):
    x=0
    y=0
    c1=0
    c2=0
    for i in l:
        if i['month']<=6:
            if i['MNTM']!=-9999:
                x+=i['MNTM']
                c1+=1
        if i['month']>=7:
            if i['MNTM']!=-9999:
                y+=i['MNTM']
                c2+=1
    print('Overall: {:.1f}'.format((x+y)/(c1+c2)))
    if c1>3:
        print('First 6 months: {:.1f}'.format(x/c1))
    else:
        print('First 6 months: Not enough data')
    if c2>3:
        print('Last 6 months: {:.1f}'.format(y/c2))
    else:
        print('Last 6 months: Not enough data')
#histogram function => print histograms for four quarters of a given year
def histogram(l):
    x=0
    y=0
    z=0
    k=0
    c1=0
    c2=0
    c3=0
    c4=0
    for i in l:
        if i['month']<=3:
            if i['MNTM']!=-9999:
                x+=i['MNTM']
                c1+=1
        if i['month']>3 and i['month']<=6:
            if i['MNTM']!=-9999:
                y+=i['MNTM']
                c2+=1
        if i['month']>6 and i['month']<=9:
            if i['MNTM']!=-9999:
                z+=i['MNTM']
                c3+=1
        if i['month']>9 and i['month']<=12:
            if i['MNTM']!=-9999:
                k+=i['MNTM']
                c4+=1
    if c1>=2:
        print('01-03: {}'.format('*'*int(x/c1)))
    else:
        print('01-03: Not enough data')
    if c2>=2:
        print('04-06: {}'.format('*'*int(y/c2)))
    else:
        print('04-06: Not enough data')
    if c3>=2:
        print('07-09: {}'.format('*'*int(z/c3)))
    else:
        print('07-09: Not enough data')
    if c4>=2:
        print('10-12: {}'.format('*'*int(k/c4)))
    else:
        print('10-12: Not enough data')

#MAIN CODES
if __name__ == '__main__':
    data = json.loads(open('tempdata.json').read())
    Y=int(input('Enter a year (1956-2015) => '))
    print(Y)
    print('Temperatures')
    print('-'*70)
    y=[]
    find_year(Y)
    hl_temperatures(y)
    max_temperatures(y)
    print()
    print('Precipitation')
    print('-'*70)
    hlts_precipitation(y)
    print()
    print('Average temperatures')
    print('-'*70)
    ave_temperatures(y)
    print()
    print('Temperature histograms')
    print('-'*70)
    histogram(y)