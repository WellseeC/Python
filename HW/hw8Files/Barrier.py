'''
class Bird deal with the information and situations barriers will have in the game
'''
class Barrier(object):
    #Basic information
    def __init__(self,n,s,x0,y0,r):
        self.name=n
        self.strength=float(s)
        self.x=float(x0)
        self.y=float(y0)
        self.radius=float(r)
    #Situation barriers will have when they have collisions with birds
    def c_bird(self,bird):
        d=bird.mass*(bird.dx**2+bird.dy**2)
        self.strength-=d
        if self.strength<0.0:
            self.strength=0.0