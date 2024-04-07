'''

Sample Input
7 50
1 12 5 111 200 1000 10
Sample Output
4

'''

n = int(input("Enter n: "))
arr = []
count = 0
max_amount = int(input("Enter the maximum amount: "))
print("Enter the array elements: ")
for i in range(n):
    arr.append(int(input()))
#sorting using selection sort
'''
for i in range(len(arr)-1):
    for j in range(i+1,len(arr)):
        if arr[i] > arr[j]:
            arr[j], arr[i] = arr[i],arr[j]
'''
arr.sort()
sum = arr[0]
for i in range(1, len(arr)):
    if sum < max_amount:
        sum +=  arr[i]
        count += 1
print(count)
