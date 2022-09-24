#find min of given array
arr = [10,20,30,4,1,0,-9]
minval=-999999999999
for i in range(len(arr)):
    if(minval<arr[i]):
        minval=arr[i]
print(minval)
