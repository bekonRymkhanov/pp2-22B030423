import time
needs_list=list(input("write products list to buy:").split(","))
time.sleep(2)
print("you returned to your house after shop,")
time.sleep(2)
buyed_list=list(input("write productes you buyed:").split(","))
for i in buyed_list:
    if i in needs_list:
        needs_list.remove(i)
    else:
        print(f"why you buy {i} ,stupid")
print("you forgot:",end="")
for i in range(len(needs_list)):
    print(needs_list[i],end=",")
    