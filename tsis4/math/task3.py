import math
def area_of_polygon(sides,lenght):
    apothem=(lenght/2)/math.tanh(180/sides)
    print(apothem)
    return apothem*sides*lenght/2
print(area_of_polygon(4,25))