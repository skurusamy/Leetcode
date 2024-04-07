s = input("Enter the string: ")
occ = int(input("Enter the occurrence of the characters: "))
hash = {}
count = 0
for i in s:
    if i not in hash:
        hash[i] =  1
    else:
        hash[i] += 1
for i in hash:
    if hash[i] == occ:
            count += 1
print(count)