import sys
nums = [-2,1,-3,4,-1,2,1,-5,4]
currsum = nums[0]
maxSum = nums[0]
for i in range(1,len(nums)):
    currsum = max(currsum + nums[i],nums[i])
    maxSum = max(maxSum,currsum)
print(maxSum)

