"""
This program experiments with the use of functions
and also learning error checking.


"""

## Function returns the length of a line 
## starting at (x1,y1) and ending at (x2,y2)
import math
def line_length(initial_x,initial_y,next_x,next_y):
    length = (initial_x-next_x)**2 + (initial_y-next_y)**2
    length = math.sqrt(length)
    return length

initial_x = 10
initial_y = 10
next_x = int(input("The next x value ==> "))
next_y = int(input("The next y value ==> "))

print("The line has moved from ({:.0f},{:.0f}) ".format(initial_x,initial_y),"to ({:.0f},{:.0f})".format(next_x,next_y))

length = line_length(initial_x,initial_y,next_x,next_y)

print('Total length traveled is:',round(length,2))