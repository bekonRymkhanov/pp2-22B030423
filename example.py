def isprime(x:int):
    if x<2:
        return False
    for i in range(2,x//2+1):
        if(x%i==0):
            return False
    return True
first_list=[]
second_list=[]
size=int(input("number till:"))
for i in range(size):
    if isprime(i):
        first_list.append(i)
print(first_list)
for i in range(1,len(first_list)+1):
    if isprime(i):
        print(first_list[i-1],end=",")

