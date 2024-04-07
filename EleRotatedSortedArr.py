def findEle(arr,left,right,ele):
    mid = (left + right) // 2
    if left > right:
        return -1
    if arr[mid] == ele:
        return mid
    if arr[left] <= arr[mid]: # left array is sorted
        if ele >= arr[left] and ele <= arr[mid]:
            return findEle(arr, left, mid-1, ele)
        else:
            return findEle(arr, mid+1,right,ele)
    else:
        if ele >= arr[mid] and ele <= arr[right]:
            return findEle(arr, mid+1,  right, ele)
        else:
             return findEle(arr, left, mid-1, ele)





#arr = [5,6,1,2, 3, 4]
arr = [15,16,17,18,1,3,5,6,7]
ele = 17
print(findEle(arr,0,len(arr)-1,ele))