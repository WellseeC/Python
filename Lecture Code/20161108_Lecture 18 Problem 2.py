import math

class Point2d(object):
    def __init__( self, x0, y0 ):
        self.x = x0
        self.y = y0
    def magnitude(self):
        return math.sqrt(self.x**2 + self.y**2)
    def dist(self, o):
        return math.sqrt( (self.x-o.x)**2 + (self.y-o.y)**2 )
    def scale(self,number):
        self.x=self.x*number
        self.y=self.y*number
        return self
    def dominates(p,q):
        if p.x>q.x and p.y>q.y:
            return True
        else:
            return False
    def __eq__(a,b):
        if a.x==b.x and a.y==b.y:
            return True
        else:
            return False    
    def __str__(self):
        return ('('+str(self.x)+','+str(self.y)+')')

    def __sub__(self,y):
        return ('('+str(self.x-y.x)+','+str(self.y-y.y)+')')
    
    def __mul__(self,y):
        return ('('+str(self.x*y)+','+str(self.y*y)+')')
    
if __name__ == "__main__":
    p = Point2d(0,4)
    q = Point2d(5,10)
    leng = q.magnitude()
    leng = Point2d.magnitude(q)
    print("Magnitude {:.2f}".format( leng ))
    print("Distance is {:.2f}".format( p.dist(q) ))
    p.scale(3)
    print('After scaling p = ({},{})'.format(p.x, p.y) )
    r = Point2d(3,5.5)
    r.scale(2)
    print('After scaling r = ({},{})'.format(r.x, r.y) )
    print('p dominates r:', p.dominates(r))
    print('r dominates p:', r.dominates(p))
    print('r dominates q:', r.dominates(q))
    print("As a string p is " + str(p))
    print("As a string r is " + str(r))
    print('p - q =', str(p-q) )
    print('q - r =', str(q-r) )
    new_q = q*4
    print('new_q is', new_q )
    t = Point2d(0,12)
    u = Point2d(0,5)
    v = Point2d(5,12)
    print('p == t', p==t )
    print('t == u', t==u )
    print('t == v', t==v )