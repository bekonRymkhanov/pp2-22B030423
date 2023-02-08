class Shape:
    def __init__(self,lenght):
        self.lenght=lenght
    def Area(self):
        return 0
class Squere(Shape):
    def __init__(self, lenght):
        super().__init__(lenght)
    def Area(self):
        self.area=self.lenght**2
        return self.area
class Rectangle(Shape):
    def __init__(self, lenght,width):
        Shape.__init__(self,lenght)
        self.width=width
    def Area(self):
        return self.lenght*self.width
obj=Rectangle(15,20)
print(obj.Area())
 
