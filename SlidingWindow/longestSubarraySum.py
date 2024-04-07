def longestSubarraySum(arr,target):
    if len(arr) == 0:
        return 
    start = 0
    end = 0
    sum = 0
    output = []
    while end < len(arr):
        sum += arr[end]
        if sum < target:
            end += 1
        elif sum == target:
            output.append(end - start+1)
            start += 1
            end = start 
            sum = 0
        else:
            start += 1
            end = start 

    return max(output)

arr = [4,-1,1,1,2,2,5]
target = 5
print(longestSubarraySum(arr,target))