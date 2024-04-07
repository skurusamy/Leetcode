st = input("Enter a string: ")
for i in range(len(st)):
    for j in range(i+1,len(st)+1):
        ans = st[i:j]
        print(ans)