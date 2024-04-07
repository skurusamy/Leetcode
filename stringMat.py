from collections import defaultdict
str1 = "abcedrfthghjop"
n =3
ans = defaultdict(list)
for i in range(len(str1)):
    val = i%n
    if val not in ans:
        ans[val].append(str1[i])
    else:
        ans[val].append(str1[i])
print(ans.values())