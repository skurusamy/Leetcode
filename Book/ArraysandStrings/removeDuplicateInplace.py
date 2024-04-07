#nums = [1,1,2]
nums = [0,0,1,1,1,2,2,3,3,4]
ans_ptr = 0
for i in range(1,len(nums)):
    if nums[ans_ptr] != nums[i]:
        ans_ptr += 1
        nums[ans_ptr] = nums[i]
        
        
print(nums, ans_ptr+1)
