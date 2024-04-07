'''

two sorted Array . where A has more additional space to accomodate B

'''

def sortedMerge(a,b,a_len,b_len):
    mergedIndex = a_len + b_len - 1
    a_index = a_len -1
    b_index = b_len - 1
    while b_index >= 0:
        if a_index-1 >= 0 and a[a_index] > b[b_index] :
            a[mergedIndex]  = a[a_index]
            a_index -= 1
        else:
            a[mergedIndex]  = b[b_index]
            b_index -= 1
        mergedIndex -= 1
    print(a)

a = [1,3,8,10,0,0,0,0,0]
a_len = 4
b_len = 5
b = [1,2,5,12,15]
print(a,b)
sortedMerge(a,b,a_len,b_len)
