'''
Input: nums = [1,2,3,4,5]
Output: true
Explanation: Any triplet where i < j < k is valid.
'''
nums = [5,4,3,2,1]
flag = 0
for i in range(len(nums)-2):
    if nums[i] < nums[i+1] and nums[i+1] < nums[i+2]:
        flag =1
if flag == 0:
    print("No")
else:
    print("Yes")