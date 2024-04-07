arr = [9,3,12,1,2,4]
left = 0
right = len(arr) -1
while left <= right:
    if arr[left] > arr[right]:
        arr[left], arr[right] = arr[right],arr[left]
    left += 1
    right -= 1
print(arr)
