def mulXY(x,y):
    z=0 
    for i in range(abs(y)):
        z=z+x
    if((y<0 and x<0)  or (x>0 and y>0)):
        return abs(z)
    else:
        return -abs(z)
def powXZ(x,z):
    var = 1
    for i in range(abs(z)):
        var = mulXY(var,x)
    if z <0:
        return 1/var
    return var
x=2
z=-2
print(powXZ(x,z))
