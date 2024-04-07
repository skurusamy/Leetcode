arr = [1, 3, 2, 6, -1, 4, 1, 8, 2]
k=5
ans = []
sum = 0
for i in range(len(arr) - k+1):
    for j in range(i, i+k):
        sum = sum + arr[j]
    ans.append(sum/k)
    sum = 0
print(ans)
