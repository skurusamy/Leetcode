'''
Its magic index if arr[i] = i
Consider there is no duplicate values
Can be done using binary search but the key is the index itself
'''
def findMagicIndex(arr):
    left = 0
    right = len(arr) - 1
    while(left <= right):
        mid = (left + right) // 2
        if mid == arr[mid]:
            return mid
        if mid > arr[mid]:
            left = mid +1
        else:
            right = mid -1
    #return False


def findMagicwithDistinct(arr): # since the values can be repeated, magic index can be before or after mid
#left is considered as max(previous and current element)
#right is min(current and next element)
    left = 0
    right = len(arr) - 1
    while(left <= right):
        mid = (left + right) // 2
        if mid == arr[mid]:
            return mid
        if mid > arr[mid]:
            left = max(mid,mid+1)
        else:
            right = min(mid,mid -1)


arr = [-40,-20,-1,1,2,3,5,8,8,12,13]
print(findMagicIndex(arr))
print(findMagicwithDistinct(arr))