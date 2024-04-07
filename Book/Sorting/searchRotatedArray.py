def searchRotatedArray(arr,left,right,key):
    if left > right:
        return
    mid = (left + right )//2
    if arr[mid] == key:
        return mid+1
    if arr[mid-1] < arr[mid]:# left array is sorted
        if key >= arr[left] and key <= arr[mid]:
            return searchRotatedArray(arr,left,mid-1,key)
        else:
            return searchRotatedArray(arr,mid+1,right,key)
    else:
        if key >= arr[mid] and key <= arr[right]:
            return searchRotatedArray(arr,mid+1,right,key)
        else:
             return searchRotatedArray(arr,left,mid-1,key)

             



arr = [15,16,17,18,1,5,6,7,9]
key = 7
print(searchRotatedArray(arr,0,len(arr)-1,key))