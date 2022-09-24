def smallestK(n):
    # code here
    # retured value will be printed by driver code
    fact = []
    if(n==1):
        return 1
    while(n>1):
        #print(n)
        for i in range(9,1,-1):
            if(n%i==0):
                fact.append(i)
                n=n//i 
                break
        return -1
    fact = sorted(fact)
    ans = "".join(map(str,fact))
    return int(ans)
test = [26,9,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25]
for i in test:
    print(smallestK(i))