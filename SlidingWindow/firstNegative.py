def subsetSum(arr,k):
    if len(arr) <= k:
        return sum(arr)
    start = 0
    end = 0
    ans = 0
    output = []
    while end < len(arr):
        if end - start +1 < k:
            end += 1
        elif end - start + 1 ==k:
            for i in range(start,end+1):
                if arr[i] < 0:
                    output.append(arr[i])
                    break
            start += 1
            end += 1
    return output
        

arr = [2,-1,-7,8,-15,30,13,28]
k = 3
print(subsetSum(arr,k))