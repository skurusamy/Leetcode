def twoSum(nums,target):
    ans = []
    if len(nums) == 0:
        return ans
    for i in nums:
        second_val =  target - i
        if second_val in nums and nums.index(i) != nums.index(second_val):
            ans.append(nums.index(i))
            ans.append(nums.index(second_val))
            return ans
    


nums = [3,2,4]
target = 6
print(twoSum(nums, target))