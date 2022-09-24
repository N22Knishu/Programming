
def fib(n):
    res=[]
    a,b=0,1
    while a<n:
        res.append(a)
        a,b=b,a+b
    return res

def prime(n):
    res=[]
    cnt = 0
    for i in range(2,n):
        cnt = 0
        for j in range(2,i):
            if(i%j==0):
                break
        else:
            if(cnt==n):
                return res
            res.append(i)
            cnt+=1
    return res
n = int(input())
flist = fib(n)
plist = prime(n)
i=0
j=0
k=0
minlen = min(len(flist),len(plist))
while(i < minlen):
    if(i%2==0):
        print(flist[j],end=" ")
        j+=1
    else:
        print(plist[k],end=" ")
        k+=1
    i+=1