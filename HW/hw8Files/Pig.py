'''
class Pig deal with the information of the positions of pigs in the game 
'''
class Pig(object):
    #Basic information of pigs
    def __init__(self,n,x0,y0,r):
        self.name=n
        self.x=float(x0)
        self.y=float(y0)
        self.radius=float(r)
        