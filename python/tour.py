n=int(input())
k=int(input())
plan = list()
ans = [0]*n
ctour = {}
for i in range(k):
    rows=list(map(int,input().split()))
    plan.append(rows)
for i in range(n):
    ctour[i] = 0
for i in range(k):
    for j in range(n):
        if(plan[i][j]==1):
            ctour[j]+=1
print(ctour)




