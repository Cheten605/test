class Point:
    def __init__ (self, initX, initY):
        self.x = initX
        self.y = initY
    def getX(self):
        return self.x
    def getY(self):
        return self.y
    def __str__(self):
        return f"X : {self.x}, y = {self.y}"
    
    def halfway(self, target):
        mx = (self.x + target.x)/2
        my = (self.y + target.y)/2
        return Point(mx, my)
    
p = Point(2, 4)
q = Point(6, 8)

midpoint = p.halfway(q)
print (midpoint)
print(midpoint.getX())
print(midpoint.getY())




    