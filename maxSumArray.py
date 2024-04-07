n = int(input("Enter the size of an array: "))
arr = []
for i in range(n):
    arr.append(int(input()))
curr_max = arr[0]
max_till = arr[0]
for i in range(1,n):
    curr_max = max(arr[i], curr_max+arr[i])
    max_till = max(curr_max, max_till)
print(max_till)