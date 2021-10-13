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
def k_selection(list,k):
    li=sort(list)
    return li[k-1]
print(select_k([3,2,1,4,5],3))
