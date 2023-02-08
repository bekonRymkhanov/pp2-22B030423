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
obj=Squere(10)
print(obj.Area())
