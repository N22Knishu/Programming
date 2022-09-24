def multXandY(x,y):
    if y ==0:
        return 0
    if y>0:
        return x+multXandY(x,y-1)
    if y<0:
        return -multXandY(x,-y)
print(multXandY(3,5))