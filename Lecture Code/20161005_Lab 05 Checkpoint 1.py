import lab05_util
restaurants = lab05_util.read_yelp('yelp.txt')
def print_info(restaurant):
    address = restaurant[3].split('+')
    ave = sum(restaurant[6])/len(restaurant[6])
    print('''{} ({})
        {}
        {}
Average Score: {:.2f}'''.format(restaurant[0],restaurant[5],address[0],address[1],ave))
print_info(restaurants[0])
print_info(restaurants[4])