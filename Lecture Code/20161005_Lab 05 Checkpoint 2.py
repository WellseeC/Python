import lab05_util

def print_info(restaurant):
    address = restaurant[3].split('+')
    if len(restaurant[6])<3:
        ave = sum(restaurant[6])/len(restaurant[6])
    else:
        ave = (sum(restaurant[6])-max(restaurant[6])-min(restaurant[6]))/(len(restaurant[6])-2)
    
    print('''{} ({})
        {}
        {}'''.format(restaurant[0],restaurant[5],address[0],address[1]))
    if ave>=0 and ave<2:
        print('This restaurant is rated bad, based on {} reviews.'.format(len(restaurant[6])))
    if ave>=2 and ave<3:
        print('This restaurant is rated average, based on {} reviews.'.format(len(restaurant[6])))
    if ave>=3 and ave<4:
        print('This restaurant is rated above average, based on {} reviews.'.format(len(restaurant[6])))
    if ave>=4 and ave<5:
        print('This restaurant is rated very good, based on {} reviews.'.format(len(restaurant[6])))

restaurants = lab05_util.read_yelp('yelp.txt')

id = int(input('Enter an ID for a restaurant: '))
if id<1 or id>len(restaurants):
    print('Error')
else:
    print_info(restaurants[id-1])