def findMin(nums):
    left = 0
    right = len(nums) - 1
    while(left < right):
            mid = (left + right) // 2
            if nums[left] > nums[right]:
                left = mid 
            else:
                return nums[left]
    return -1
print(findMin([2,1]))