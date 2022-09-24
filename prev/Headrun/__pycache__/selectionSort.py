arr = [10,20,3,1,6]
for i in range(len(arr)):
    minVal = arr[i]
    for j in range(i+1,len(arr)):
        if(minVal>arr[j]):
            minVal=arr[j]
print(minVal)
