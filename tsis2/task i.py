import time
a=input("start loading?(yes or no)")
b=0
if(a=="no"):print("it was game of thrones :(")
elif(a=="yes"):
    while(b<101):
        print(b)
        b+=1
        time.sleep(0.07)
    else:
        print("we loaded a virus to your laptop :) ")
        time.sleep(1)
        print("enjoy ")
