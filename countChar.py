str = input("Enter the string: ")
occ = int(input("Enter the number: "))
hash = {}
count =0
for i in range(len(str)):
    if str[i] not in hash:
        hash[str[i]] = 1
    else:
        hash[str[i]] += 1
for i in hash:
    if hash[i] == occ:
        count += 1
        print(i)
print(count)