def subsetSum(arr,k):
    if len(arr) <= k:
        return sum(arr)
    start = 0
    end = 0
    ans = 0
    output = []
    while end < len(arr):
        ans += arr[end]
        if end - start +1 < k:
            end += 1
        elif end - start + 1 ==k:
            output.append(ans)
            ans -= arr[start]
            start += 1
            end += 1
    return max(output)
        

arr = [11,3,6,1,-16,2]
k = 2
print(subsetSum(arr,k))