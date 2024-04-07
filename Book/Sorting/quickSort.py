def quickSort(arr,left,right):
    curIndex = partition(arr,left,right)
    if left < curIndex - 1:
        quickSort(arr,left,curIndex-1)
    if curIndex < right:
        quickSort(arr,curIndex, right)

def partition(arr,left,right):
    pivot = arr[left + (right - left) // 2] 
    while left <= right:
        while arr[left] < pivot:
            left += 1
        while arr[right] > pivot:
            right -= 1
        if left <= right:
            arr[left] , arr[right] = arr[right],arr[left]
            left += 1
            right -= 1
    return left

arr = [100,50,80,10]
print(arr)
quickSort(arr,0,len(arr)-1)
print(arr)