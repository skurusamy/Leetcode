'''
Sample Input
5 4
1 2 3 4 5
Sample Output
5 1 2 3 4
'''

n = int(input("Enter n: "))
d = int(input("Enter digits to rotate: "))
arr = []
print("Enter the array elements: ")
for i in range(n):
    arr.append(int(input()))
res = [0] * len(arr)
for i in range(n):
    newIndex = (i - d) % n
    res[newIndex] = arr[i]
print(res)