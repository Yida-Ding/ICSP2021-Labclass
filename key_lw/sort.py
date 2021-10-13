def sort(list):
    if(len(list)<=1):
        return list
    mid=[]
    mid.append(list[0])
    del list[0]
    left=[]
    right=[]
    for i in list:
        if(i<=mid[0]):
            left.append(i)
        else:
            right.append(i)
    return sort(left)+mid+sort(right)
print(sort([3,5,2,1,6,9,7,8,0]))
