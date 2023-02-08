def unique(my_list):
    new_list=list()
    for i in my_list:
        if new_list.count(i)==0:
            new_list.append(i)
    return new_list
print(unique([1,2,3,4,5,5,5,6,3,4,7,8,3]))
