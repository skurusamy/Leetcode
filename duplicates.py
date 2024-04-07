n = int(input("Enter the size of the array: "))
a = []
seen = set()
for i in range(n):
    a.append(input())
for i in range(n):
    if a[i]  not in seen:
        seen.add(a[i])
    else:
        print(a[i])
        break