'''
class Bird deal with the information and situations birds will have in the game
'''
#IMPORTS
import math
class Bird(object):
    #Basic information
    def __init__(self,n,m,x0,y0,r,dx0,dy0):
        self.name=n
        self.mass=m
        self.x=float(x0)
        self.y=float(y0)
        self.radius=float(r)
        self.dx=float(dx0)
        self.dy=float(dy0)
    #Basic movement when birds fly
    def common(self):
        self.x+=self.dx
        self.y+=self.dy
    #Situation when birds have collisions with pigs 
    def c_pig(self):
        self.dx=self.dx/2
    #Situation when birds have collisions with barriers
    def c_barrier(self):
        self.dx=0.0
        self.dx=0.0
    #Birds' speed
    def speed(self):
        return math.sqrt(self.dx**2+self.dy**2)
        