def sortColors(nums):
    colored ={0:0,1:0,2:0}
    for i in range(len(nums)):
        colored[i]=nums.count(i)
    print(colored.get(0))
    print(colored.get(1))
    print(colored.get(2))
    for i in range(len(nums)):
        if(i>=0 and i<=colored.get(0)):
            nums[i]==0
        elif(i>=colored.get(0) and i<=colored.get(1)):
            nums[i]==1
        else:
            nums[i]==2
    return nums
nums=[0,0,2,1,1]
print(sortColors(nums))