n = int(input("Enter n: "))
a= []
print("Enter Elements: ")
for i in range(0,n):
    col = []
    for j in range(0,n):
        col.append(input())
    a.append(col)
print(a)
for i in range(0, n//2):
    for j in range(i, n-1-i):
        temp = a[i][j]
        a[i][j] = a[n - 1 - j][i]
        a[n - 1 - j][i] = a[n-1-i][n-1-j]
        a[n - 1 - i][n - 1 - j] = a[j][n-1-i]
        a[j][n-1-i] = temp
print(a)