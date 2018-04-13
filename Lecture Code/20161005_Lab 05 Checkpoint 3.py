import lab05_util
import webbrowser

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
id = int(input('Enter an ID for a restaurant: '))
if id<1 or id>len(restaurants):
    print('Error')
else:
    print_info(restaurants[id-1])
    next = int(input('''What would you like to do next?
    1. Visit the homepage
    2. Show on Google Maps
    3. Show directions to the restaurant
    Your choice (1-3)? ==>'''))
    if next == 1:
        webbrowser.open(restaurants[id-1][4])
    elif next == 2:
        webbrowser.open('http://www.google.com/maps/place/{}'.format(restaurants[id-1][3]))
    elif next == 3:
        webbrowser.open('http://www.google.com/maps/dir/110 8th Street Troy NY/{}'.format(restaurants[id-1][3]))
    else:
        print('Error')

restaurants = lab05_util.read_yelp('yelp.txt')