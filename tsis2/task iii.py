a =int(input("enter a number:"))
b=0
if(a<2):print("doesnt have one")
else:
    for i in range (2,a+1):
        for j in range (2,(i-1)):
            if(i%j==0):
                b+=1
        if(b==0):
            print(i)
        else:
            b=0
              
