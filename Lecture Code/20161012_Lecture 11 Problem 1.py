def earlier_semester(x,y):
    x = list(x)
    y = list(y)
    if x[0] > y[0] and x[1] == y[1] or x[0] == y[0] and x[1] < y[1] or x[0] > y[0] and x[1] > y[1] or x[0] < y[0] and x[1] < y[1]:
        return('True')
    else:
        return('False')
w1 = ('Spring',2015)
w2 = ('Spring',2014)
w3 = ('Fall', 2014)
w4 = ('Fall', 2015)
print( "{} earlier than {}? {}".format( w1, w2, earlier_semester(w1,w2)))
print( "{} earlier than {}? {}".format( w1, w1, earlier_semester(w1,w1)))
print( "{} earlier than {}? {}".format( w1, w4, earlier_semester(w1,w4)))
print( "{} earlier than {}? {}".format( w4, w1, earlier_semester(w4,w1)))
print( "{} earlier than {}? {}".format( w3, w4, earlier_semester(w3,w4)))
print( "{} earlier than {}? {}".format( w1, w3, earlier_semester(w3,w2)))