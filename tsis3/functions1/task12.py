def histogram(nums):
    for i in nums:
        for j in range(i):
            print('*',end='')
        print('')
histogram([1,2,3,4])
