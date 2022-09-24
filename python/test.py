arr = [2,1,99,3,8,7,6,12,11]
'''print(dir(arr))
maxNum = max(arr)
index = arr.index(maxNum)
#index = (arr,maxNum)
print(index)
for j in range(index,len(arr),2):
    print(arr[j])'''

for i in range(len(arr)-1):
    if(arr[i]>arr[i+1]):
        arr[i+1],arr[i]=arr[i],arr[i+1]
print(arr)

