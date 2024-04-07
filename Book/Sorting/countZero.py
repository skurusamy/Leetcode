def countZero(arr,left,right):
    if left > right:
        return
    while left < right:
        mid = (left + right) //2
        if arr[mid] == 1 and arr[mid-1] == 0 and arr[mid+1] == 1:
            return mid
        if  arr[mid+1] == 0:
            return countZero(arr,mid+1,right) 
        return countZero(arr,left,mid)

arr = [0,0,0,0,0,0,1,1]
print(countZero(arr,0,len(arr)))
