fruits = []
print("how many favorite things do you have?")
b=int(input())

for i in range(b):
    print("name the",i+1,"element")
    x=input()
    fruits.append(x)
fruits.reverse()
for i in fruits:
    print(i)
