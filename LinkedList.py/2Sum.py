arr = [1,2,7,8,11,15]
target = 9
left = 0
right = len(arr) - 1
while left < right:
    if arr[left] + arr[right] > target:
        right -= 1
    elif arr[left] + arr[right] < target:
        left += 1
    else:
        print(left,right)
        left += 1
        right -= 1
