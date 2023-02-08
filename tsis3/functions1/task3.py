def solve(numheads,numlegs):
    for i in range(numheads+1):
        if ((numheads-i)*2)+i*4==numlegs:
            return i,numheads-i
x,y=solve(6,20)
print(f"rabbits:{x},chickens:{y}")
