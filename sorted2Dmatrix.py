def merge(left,right):
    i,j= 0, 0
    ans =[]
    while(i < len(left) and j< len(right)):
        if left[i] < right[j]:
            ans.append(left[i])
            i+=1
        else:
            ans.append(right[j])
            j+=1
    while(i<len(left)):
        ans.append(left[i])
        i +=1
    while(j<len(right)):
        ans.append(right[j])
        j += 1
    return ans

def mergeAlt(left,right):
    idx = 0
    i = 0
    j = 0
    while i < len(left) and j < len(right):
        if left[i] >= right[j] :
            left.insert(idx,right[j])
            j += 1
        i += 1
        idx += 1
    print(left)
    while j < len(right):
            left.insert(idx,right[j])
            j += 1
            idx += 1
    return left

l = [[10,20],[15, 25], [27, 29],[ 32, 33]]
result = l[0]
for next in l[1:len(l)]:
    result = mergeAlt(result,next)
print(result)