import sys
nums = [-4,-1,0,3,10]
for i in range(1, len(nums)):
    sortedIndex = i
    for j in range(sortedIndex,0,-1):
        if nums[j] < nums[j-1]:
            nums[j-1] , nums[j] = nums[j] , nums[j-1]
print(nums)