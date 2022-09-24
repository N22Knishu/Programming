
def common_elements(list1, list2, list3):
    res = sorted(set(list1) & set(list2) & set(list3))
    if(len(res)==0):
        return "no common elements"
    else:
        for i in res:
            print(i,end=" ")
n1 = int(input())
list1 = list(map(int, input().split()))
n2 = int(input())
list2 = list(map(int, input().split()))
n3 = int(input())
list3 = list(map(int, input().split()))
common_elements(list1, list2, list3)
