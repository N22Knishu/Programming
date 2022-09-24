def getNearestNum(nums,target):
        start,n = 0, len(nums)
        end = n
        while(start<end):
            mid = (start+end)//2
            if(nums[mid]>=target):
                end= mid 
            else:
                start = mid + 1 #remove -1 for strict upper_bound 
        return start
def findNumOfPair(array, n): 
    count = 0
    for i in range(len(array)):
        target = 0
        if(array[i]>=0):
            target=array[i]
        else:
            target=array[i]*-1+1
        k=getNearestNum(array,target)
        if(k==i):
            k+=1
        if(k<=n):
            count+=n-k  
    return count
print(findNumOfPair(sorted([3,-2,1]),3))
