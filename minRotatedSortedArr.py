'''
Find the minimum element in a sorted and rotated array
Can be done in O(n) but try using Binary search - O(log n)
'''

def findMin(arr,left,right):
    mid = (left + right ) // 2
    if left == right:
        return arr[left]
    if arr[mid] < arr[left]:
        return arr[mid]
    elif arr[mid] < arr[right]:
        return findMin(arr,left,mid)
    elif arr[mid] > arr[right]:
        return findMin(arr,mid+1,right)
#arr = [2,1]
arr = [2, 3, 4,1]
print(findMin(arr,0,len(arr)-1))