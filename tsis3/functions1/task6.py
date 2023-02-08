def reverse(sent:str):
    my_list=list(sent.split(" "))
    my_list.reverse()
    for i in my_list:
        print(i,end=" ")
reverse("hello my name is bekarys")
