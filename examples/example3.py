# class Mynumber:
    
#     def __iter__(self):
#         self.a=1
#         return self
#     def __next__(self):
#         x=self.a
#         self.a+=1
#         return x
# myclass=Mynumber()
# myiter=iter(myclass)
# next(myiter)
# print(next(myiter))
# print(next(myiter))
# print(next(myiter))



# def it(ob):
#     try:
#         iter(ob)
#         return True
#     except:
#         return False
    
# for i in [34,[2,4],(3,2),{"a":1},"asd",3.25]:
#     print( i, " is iterable" ,it(i))

import re

f=open("text.txt","r")
print(f.readline().rstrip())

