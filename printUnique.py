num = int(input("Enter number: "))
l = 1
r = num+1
for i in range(l,r):
    n = i
    visited = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
    while n > 0:
        val = n % 10
        if visited[val % 10] != 1:
            visited[val %10] = 1
        else:
            break
        n = n // 10
    if n == 0 :
        print(i)