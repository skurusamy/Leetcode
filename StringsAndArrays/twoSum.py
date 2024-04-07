'''
Input: nums = [2,7,11,15], target = 9
Output: [0,1]
Explanation: Because nums[0] + nums[1] == 9, we return [0, 1].

'''
'''
# n square
def findTwoSums(nums,target):
    for i in range(len(nums)):
        for j in range(len(nums)):
            if nums[i] + nums[j] == target and i != j:
                return [i,j]
'''
#log n
def findTwoSums(nums,target):
    start = 0
    end = len(nums) -1
    while start < end:
        if nums[start] + nums[end] < target:
            start += 1
        elif nums[start] + nums[end] > target:
            end -= 1
        else:
            return [start,end]
    return 


    
nums = [2,7,11,15]
target = 9
print(findTwoSums(nums, target))


