def LIS(arr):
    #seq = set()
    if len(arr) == 0:
        return 0
    ans = [1] * len(arr)
    i = 1
    while i < len(arr):
        for j in range(i):
            if arr[i] > arr[j]:
                ans[i] = max(ans[i],ans[j]+1)
                #seq.add(arr[i])
            else:
                break
        i += 1
    return max(ans)

arr = [10,22,9,33,21,50,41,60]
print(LIS(arr))