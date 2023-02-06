my_tuple = tuple(input("write thomthing:"))
chracters = dict()
for i in my_tuple:
    chracters[i]=my_tuple.count(i)
for i,j in chracters.items():
    if i==' ':
        i="space"
    print(f"{i} character is repeated {j} times")
