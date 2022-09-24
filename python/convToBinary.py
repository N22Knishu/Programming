from StackOf import StackOf
def convToBinary(data):
    msb = StackOf()
    res = ""
    print(data)
    while(data!=0):
        bit = data%2
        data = data//2
        msb.push(bit)
    while((not msb.is_empty())):
        res = res+str(msb.pop())
    return res
input = 15
print(convToBinary(input))

