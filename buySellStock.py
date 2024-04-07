arr = [7,1,5,3,6,4]
profit = 0
for i in range(len(arr)-1):
    if arr[i+1] > arr[i]:
        profit += arr[i+1] - arr[i]
print(profit)   