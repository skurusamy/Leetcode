nums = [-4,-1,0,3,10]

output = [0] * len(nums)
i = 0
j = len(nums)-1
for k in range(len(output)-1,-1,-1):
    if abs(nums[i]) < abs(nums[j]):
        output[k] = nums[j] ** 2
        j -= 1
    else:
        output[k] = nums[i] ** 2
        i += 1
print(output)
