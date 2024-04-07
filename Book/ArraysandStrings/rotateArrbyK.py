nums = [1,2,3,4,5,6,7]
#Output: [5,6,7,1,2,3,4]
count =0
print(nums)
k = 6
while True:
    curVal = nums[len(nums)-1]
    curIndex = nums.index(curVal)
    for i in range(curIndex,0,-1):
        nums[i] = nums[i-1]
    nums[0]= curVal
    count += 1
    if count == k:
        break

print(nums)