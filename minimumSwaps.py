'''

Sample Input 0
4
4 3 1 2
Sample Output 0
3

Swapping to its original position directly

'''

n = int(input("Enter n: "))
arr = []
count =0
for i in range(n):
    arr.append(int(input()))
i=0
while i<len(arr):
    print(arr)
    if arr[i] != i+1:
        a = arr[arr[i]-1]
        arr[arr[i]-1] = arr[i]
        arr[i] =  a
        i = i-1
        count += 1
    i += 1
print(count)