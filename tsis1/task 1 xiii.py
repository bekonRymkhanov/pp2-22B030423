def volume_cone():
    radius =int(input("enter a radius:"))
    height =int(input("enter a height:"))
    print(1.04719756*radius**2*height)

def volume_sphere():
    radius =int(input("enter a radius:"))
    print(4.18879*radius**3)

def volume_cylinder():
    radius =int(input("enter a radius:"))
    height =int(input("enter a height:"))
    print(3.141592*radius**2*height)

def volume_cube():
    height =int(input("enter a height of first side:"))
    height2 =int(input("enter a height of second side:"))
    height3 =int(input("enter a height of third side:"))
    print(height*height2*height3)
figure=input('''volume of what are you looking for?\n1)cone\n2)sphere\n3)cylinder\n4)cube\n''')
if figure==("1" or "1)"):
    volume_cone()
elif figure==("2" or "2)"):
    volume_sphere()
elif figure==("3" or "3)"):
    volume_cylinder()
elif figure==("4" or "4)"):
    volume_cube()
else:
    print("not recognized")
