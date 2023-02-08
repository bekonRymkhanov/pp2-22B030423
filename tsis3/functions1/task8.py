def spy_game(nums):
    something=[0,0,7]
    j=0
    for i in nums:
        if i==something[j]:
            j+=1
            if j==3:
                return True
            continue
    return False

        
print(spy_game([1,2,4,0,0,7,5]))
print(spy_game([1,0,2,4,0,5,7]))
print(spy_game([1,7,2,0,4,5,0]))
print(spy_game([3,5,0,3,9,4,0,7]))
