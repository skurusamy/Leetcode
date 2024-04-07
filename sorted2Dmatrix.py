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



l = [[10,20],[15, 25], [27, 29],[ 32, 33]]
result = l[0]
for next in l[1:len(l)]:
    result = merge(result,next)
print(result)