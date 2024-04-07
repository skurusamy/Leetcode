import sys
def threeSumClosest( nums, target):
        result = nums[0] + nums[1] + nums[len(nums) - 1]
        nums.sort()
        for i in range(len(nums)-2):
            left = i + 1
            right = len(nums) - 1
            while left < right:
                sum = nums[i] + nums[left] + nums[right]
                if sum > target:
                    right -= 1
                if sum < target:
                    left += 1
                if(abs(target - sum) < abs(target - result)):
                    result = sum
        return result

print(threeSumClosest([0,1,2,4],3))