first=list(input())
second=list()
for x in first:
    d=ord(x)
    if d>=48 and d<=57:
        second.append(x)
for i in second:
    print(i,end="")
    
