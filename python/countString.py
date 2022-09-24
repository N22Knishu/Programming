#AABBBCCDDDAAA->A2B2C2D3A3

from itertools import count


def countStr(s):
    j=0
    cnt=1
    ans=""
    for i in range(len(s)-1):
        if(s[i]==s[i+1]):
            cnt+=1
        else:
            ans+=s[i]+str(cnt)
            cnt=1
    return ans+s[i]+str(cnt)
print(countStr("AAABBCCC"))
    

