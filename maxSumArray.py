import sys
arr = [2, 3, 4, 1, 5]
k=2
start = 0
res = -sys.maxsize
sum = 0
for end in range(len(arr)):
    sum += arr[end]
    end += 1
    if end >= k:
        res = max(res,sum)
        sum -= arr[start]
        start += 1
print(res)