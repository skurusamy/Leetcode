
def getLength(arr,key):
    length = 1
    for i in arr:
        if elementAt(i) != -1 and length < key:
            length *= 2
    return length

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

def elementAt(i):
    if i >10: 
        return -1
    else: 
        return i

arr = [1,2,3,4,5,6,7,8,9,10]
key = 6
length = getLength(arr,key)
#print(length)
print(binarySearchRec(arr,length//2,length,key))