import math
class Point:
    def __init__(self,x,y):
        self.x=x
        self.y=y
    def show(self):
        return self.x,self.y
    def move(self,a,b):
        self.x=a+self.x
        self.y=b+self.y
    def change(self,c,d):
        self.x=c
        self.y=d
    def dist(poi1,poi2):
        print(math.sqrt(pow(poi1[0]-poi2[0],2)+pow(poi1[1]-poi2[1],2)))
point1=Point(1,1)
print(point1.show())
point1.move(-1,-5)
print(point1.show())
point1.change(0,0)
print(point1.show())
point2=Point(3,4)
Point.dist(point1.show(),point2.show())      
