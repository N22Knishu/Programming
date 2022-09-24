from StackOf import StackOf
def revStr(str):
    res = ""
    s=StackOf()
    index = 0
    while index <len(str):
        s.push(str[index])
        index=index+1
    for i in range(len(str)):
        res+=s.pop()
    return res
k = "DLROW"
print(revStr(k))
    
