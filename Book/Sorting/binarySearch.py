def binarySearchItr(arr,key):
    left = 0
    right = len(arr)
    while left < right:
        mid = (right+left) // 2
        if arr[mid] == key:
            return mid+1
        elif arr[mid] < key:
            left = mid+1
        else:
            right = mid
    return -1

def binarySearchRec(arr,left,right,key):
    if left >= right:
        return
    mid  = (right + left)//2
    if arr[mid] == key:
        return mid+1
    elif arr[mid] > key:
        return binarySearchRec(arr,left,mid,key)
    else:
        return binarySearchRec(arr,mid+1,right,key)
    


arr=[1,2,3,4,5,6,7,8,9,10]
print(arr)
key = 20
#print(binarySearchItr(arr,key))
print("20:",binarySearchRec(arr,0,len(arr),key))
print("2:",binarySearchRec(arr,0,len(arr),2))