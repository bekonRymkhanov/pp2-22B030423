def isprime(x):
    if x<2:
        return False
    for i in range(2,int(x/2)+1):
        if x%i==0:
            return False
    return True
my_list=[1,2,3,4,5,6,7,8,9]
new_list=list(filter(lambda x:isprime(x),my_list))
print(new_list)
