'''
Input: nums = [-1,0,1,2,-1,-4]
Output: [[-1,-1,2],[-1,0,1]]
'''
nums = [-1,0,1,2,-1,-4]
visited = set()
dic = {}
ans =[]
for i in nums:
    if i not in dic:
        dic[i] = 1
    else:
        dic[i] += 1
for i in range(len(nums)):
    for j in range(i+1,len(nums)):
        comp = -nums[i] - nums[j]
        if comp not in dic:
            continue
        if dic[comp] != 0 and dic[nums[i]]!=0 and dic[nums[j]]!=0 and i != j and i != nums.index(comp) and j != nums.index(comp):
            dic[comp] -= 1
            dic[nums[i]] -= 1
            dic[nums[j]] -= 1
            ans.append(nums[i])
            ans.append(nums[j])
            ans.append(comp)
            print(ans)
            ans.clear()
