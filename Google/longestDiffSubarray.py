def longestSubarray( nums, limit):        
        start = end = 0
        maxi= mini = nums[0]
        ans = 0
        queue =[nums[0],]
        while(end < len(nums)):
            if abs(maxi -  mini) <= limit:
                ans += 1
                if end +1 < len(nums):
                    end = end +1
                    queue.append(nums[end])    
            else:
                queue.pop(0)
                start += 1
            maxi = max(queue)
            mini = min(queue)
        return ans

nums = [10,1,2,4,7,2]
limit = 5
print(longestSubarray( nums, limit))