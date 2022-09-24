def RotateStr(str1):
    return str1[len(str1)-1:]+str1[0:-1]
    
str1 = "aabc"
str2 = "aabc"
res = 0
str3=str1
print(str3)
for i in range(len(str2),0,-1):
    if(str3==str2):
        break  
    str3=RotateStr(str3)
    print(str3)
    res=res+1
    
print(res)


