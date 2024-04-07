arr = [1,2,3,4,5,6]
target = 6
left = 0
right = len(arr) - 1
while left < right:
    if arr[left] + arr[right] <  target:
        left += 1
    elif arr[left] +  arr[right] > target:
        right -= 1
    else:
        print(arr[left],arr[right])
        left += 1
        right -=1