j='aA'
s='aAAAAp'
count =0
jewels = set()
for i in j:
    if i not in jewels:
        jewels.add(i)
print(jewels)
for j in s:
    if j in jewels:
        count += 1
print(count)