

class Point:
    def __init__(self, initX, initY):#this is for storing the data and it only return NONE
        self.x = initX
        self.y = initY
        
    def getX(self):#this is made to get X coordinate and Y coordinate
        return self.x
    def getY(self):
        return self.y
    def distanceFromOrigin(self):
            return ((self.x ** 2)+ (self.y ** 2))** 0.5
def distance(point1, point2):
     xdiff = point2.getX()-point1.getX()
     ydiff = point2.getY()-point1.getY()
     return (xdiff**2 + ydiff**2)**0.5# we can import math and use math.sqrt in this line. 

    
p = Point(4, 3)
q = Point(0, 0)
print (distance(q,p))

#this is good actually !!!!
# --- IGNORE ---



