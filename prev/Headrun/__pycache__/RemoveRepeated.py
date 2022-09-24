#Remove adjacent occurrences of the same character in a string [‘ABBABCC’ to ‘AAB’ to ‘B’]

def removeRepeated(s):
    n=len(s)
    i=0
    while(i<len(s)-1 ):
        print(i)
        if(s[i]==s[i+1]):
            s=s[0:i]+s[i+2:]
            print(s)
            i=i-1 if i >1 else 0
        else:
            i=i+1
    return s
print(removeRepeated("acaaabbbacdddd"))


