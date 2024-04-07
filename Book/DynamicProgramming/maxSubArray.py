import sys
nums = [-2, 1, -3, 4, -1, 2, 1, -5, 4]

maxSubArray = -sys.maxsize
for i in range(len(nums)):
    for j in range(i,len(nums)):
        maxSubArray = max(nums[i],maxSubArray+nums[j])
print(maxSubArray)



maxSubArray = [-sys.maxsize] * (len(nums))
maxSubArray[0] = nums[0]
for i in range(1,len(nums)):
    maxSubArray[i] = max(nums[i],maxSubArray[i-1]+nums[i])
print(maxSubArray[len(nums)-1])
 