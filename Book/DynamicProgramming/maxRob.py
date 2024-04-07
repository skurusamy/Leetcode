nums = [2,7,9,3,1]
maxAmount = [0] * (len(nums)+1)
maxAmount[len(nums)-1] = nums[len(nums)-1]
for i in range(len(nums)-2,-1,-1):
    maxAmount[i] = max(maxAmount[i+1],maxAmount[i+2]+nums[i])
print(maxAmount[0])