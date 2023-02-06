print(10 + 5)
print(10 - 5)
print(10 * 5)
def Factorial(x:int):
    if x==1:
        return 1
    return x*Factorial(x-1)

x=int(input())
print(Factorial(x))
