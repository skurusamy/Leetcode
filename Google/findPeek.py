"""
Example 1:

Input: nums = [1,2,3,1]
Output: 2
Explanation: 3 is a peak element and your function should return the index number 2.
Example 2:

Input: nums = [1,2,1,3,5,6,4]
Output: 5
Explanation: Your function can return either index number 1 where the peak element is 2, or index number 5 where the peak element is 6.

"""
def findPeek(nums):
    if len(nums) == 0:
        return
    left = 0
    right = len(nums)-1
    while(left < right):
        mid = left + (right - left) // 2
        if nums[mid] < nums[mid+1]:
            left = mid+1
        else:
            right = mid 
    return left
nums = [1,2,5,3,6,4]
print(findPeek(nums))