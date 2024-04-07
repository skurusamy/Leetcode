st = input("Enter the string ")
l=[]
for i in range(len(st)):
    if st[i] in l:
        l.remove(st[i])
    else:
        l.append(st[i])
if len(l) == 0 or len(l) == 1:
    print("Palindrome")
else:
    print("No")