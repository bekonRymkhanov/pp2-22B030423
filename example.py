class Clothes:
    def __init__(self,name, size ,color,price):
        self.name = name
        self.size = size
        self.color = color
        self.price = price

    def display_info(self):
        print(f"Name:{self.name}")
        print(f"size:{self.size}")
        print(f"color:{self.color}")
        print(f"price:{self.price}")

Cloth=Clothes(name="asfasd",size=33,color="black",price=3.44)
Cloth.display_info()
