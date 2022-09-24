def updateSortedArr(num, arr):
    if(len(arr)==0):
        arr.append(num)
        return
    if(arr[0]>num):
        arr.insert(0,num)
        return
    if(arr[-1]<num):
        arr.append(num)
        return
    for i in range(len(arr)):
        if(arr[i]<num):
            arr.insert(i,num)
            return
def removeNumFromArray(num, arr):
    arr = [i for i in arr if i!=num]
    return arr
def getScore(start,end,M, K, arr):
    psum ,nsum =0,0
    pend = 0
    for i in range(0,len(arr)):
        if(arr[i]<0):
            psum+=arr[i]
        else:
            pend = i +1
    nsum = sum(arr[pend:])
    ans =0
    nlen = K - pend
    #print(parr,narr)
    if(abs(nsum)<psum or (abs(nsum)==psum and pend>nlen)):
        change = sum(arr[-1:-M])
        psum += change*-1
        nsum -= change * -1
        ans = abs(nsum + psum)
    if(abs(nsum)>psum or (abs(nsum)==psum and pend<nlen)):
        change = sum(arr[0:M])
        nsum += change*-1
        psum -= change
        ans = abs(nsum + psum)
    return ans


def maxScore(N,M,K,A):
    A = [int(i) for i in A]
    # Write your code here
    start ,end = 0,K-1
    maxScore = 0
    arr = sorted(A[0:K-1], reverse=True)
    while(end<N):
        updateSortedArr(A[end], arr)
        score = getScore(start,end,M, K, arr)
        maxScore = max(score, maxScore)
        removeNumFromArray(A[start], arr)
        start+=1
        end+=1
    return maxScore

print(maxScore(3,2,3,[-1,-1,-1]))