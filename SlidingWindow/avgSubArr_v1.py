arr = [1, 3, 2, 6, -1, 4, 1, 8, 2]
k=5
result = []
sum = 0
starting = 0
for ending in range(len(arr)):
    sum += arr[ending]
    ending += 1
    if ending >= k:
        result.append(sum/k)
        sum -= arr[starting]
        starting += 1
print(result)

