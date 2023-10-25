#program to find the quadrant in which the given co-ordinate lie in python . From the origin at x = 0 and y = 0,a pointy can move in four different directions. 
#There are 4 coordinates available when we think in 2-Dimension. These 2-dimensions are at X-axis and Y-axis. 
#Now based on their positive or negative nature this axis shows 4 different quadrants. This 4-Quadrants are different and are as follows.
#Quadrant in which the given coordinate lie

Working :
#According mathematics quadrants rules:

#X  is positive integer as well as Y is also positive a integer it signifies first quadrant.
#X  is negative integer but Y is positive integer it signifies second quadrant.
#X  is negative integer as well as Y is also negative integer it signifies third quadrant.
#X  is positive integer but Y is negative integer it signifies fourth quadrant.

Algorithm :

#Get value of x & y
#If ( x>0 and y>0 ) First Quadrant
#If ( x<0 and y>0 ) Second Quadrant
#If ( x<0 and y<0 ) Third Quadrant
#If ( x>0 and y>0 ) Fourth Quadrant
#If ( x=0 and y=0 ) Origin
#If ( x!=0 and y=0 ) x-axis
#If ( x>0 and y>0 ) y-axis

#Python program to find quadrant in which coordinate lie

'''Python code'''

# for initialization of coordinates
x, y = map(int, list(input("Insert the value for variable X and Y : ").split(" ")))

# find true condition of first quadrant
if x > 0 and y > 0:
    print("point (", x, ",", y, ") lies in the First quadrant")

# find second quadrant
elif x < 0 and y > 0:
    print("point (", x, ",", y, ") lies in the Second quadrant")

# To find third quadrant
elif x < 0 and y < 0: 
    print("point (", x, ",", y, ") lies in the Third quadrant")
 # To find Fourth quadrant 
elif x > 0 and y < 0:
    print("point (", x, ",", y, ") lies in the Fourth quadrant")

# To find does not lie on origin
elif x == 0 and y == 0:
    print("point (", x, ",", y, ") lies at the origin")

# On x-axis
elif y == 0 and x != 0:
    print("point (", x, ",", y, ") on x-axis")

# On y-axis
elif x == 0 and y != 0:
    print("point (", x, ",", y, ") on at y-axis")


Output
Insert the value for variable X and Y : -3 -33
point (-3, -33) lies in the Third quadrant
