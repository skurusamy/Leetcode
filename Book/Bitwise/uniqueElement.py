arr = [7, 3, 5, 4, 5, 3, 4]
for i in range(len(arr)-1):
    ans = arr[i] ^ arr[i+1]
print(ans)