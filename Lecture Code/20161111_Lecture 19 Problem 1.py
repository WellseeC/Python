from Point2d import Point2d

class Restaurant(object):
    def __init__(self, name, lat, lon, address, url, category, scores):
        self.name = name
        self.loc = Point2d(float(lon), float(lat))
        self.address = address
        self.url = url
        self.category = category
        self.reviews = scores

    def __str__(self):
        s =  '      Name: ' + self.name + '\n'
        s += '  Lat/Long: ' + str(self.loc) + '\n'
        s += '   Address: ' + self.address[0] + '\n'
        for i in range(1,len(self.address)):
            s += '            ' + self.address[i]  + '\n'
        s += '  Category: ' + self.category + '\n'
        s += 'Avg Review: {:.2f}'.format( self.average_review() )  + '\n'
        return s

    def is_in_city(self, city_name):
        lastLine = self.address[-1].split(',')
        city = lastLine[0].strip()
        return city.lower() == city_name.lower()

    def average_review(self):
        if len(self.reviews) == 0:
            return -1
        else:
            avg=sum(self.reviews) / len(self.reviews)
            return avg

    def min_review(self):
        l=[]
        l.append(self.reviews)
        l.sort()
        self.reviews=l[0]
        if len(self.reviews) == 0:
            return -1
        return min(self.reviews)

    def max_review(self):
        l=[]
        l.append(self.reviews)
        l.sort()
        self.reviews=l[-1]
        if len(self.reviews) == 0:
            return -1
        return max(self.reviews)

    def latitude(self):
        return self.loc.y

    def longitude(self):
        return self.loc.x

    def findtype(self):
        l=[]
        if 'American' in self.catagory and avg>3:
            l.append(self.catagory)
        else:
            l=l
        return l
    
avg=0
if __name__ == "__main__":
    n = "Uncle Ricky's Bagel Heaven"
    lat = 42.73
    lon = -73.69
    address = [ '1809 5th Ave', 'Troy, NY 12180']
    url = "http://www.yelp.com/biz/uncle-rickys-bagel-heaven-troy"
    rest_type = 'Bagels'
    reviews = [ 5, 3, 5, 4, 3, 5, 4 ]
    rest1 = Restaurant( n, lat, lon, address, url, rest_type, reviews )

    n = "No Longer In Business"
    lat = 42.74
    lon = -73.7
    address = [ '123 Nowhere Street', 'Troy, NY 12180']
    url = "http://www.not_a_valid_url.biz/snafu"
    rest_type = 'Concrete'
    reviews = [ ]
    rest2 = Restaurant( n, lat, lon, address, url, rest_type, reviews )

    print("First restaurant:")
    print("Name:", rest1.name)
    print("Latitude:", rest1.latitude() )
    print("Longitude:", rest1.longitude() )
    print("Min review:", rest1.min_review() )
    print("Max review:", rest1.max_review() )

    print("\nSecond restaurant:")
    print("Name:", rest2.name)
    print("Latitude:", rest2.latitude() )
    print("Longitude:", rest2.longitude() )
    print("Min review:", rest2.min_review() )
    print("Max review:", rest2.max_review() )
    
