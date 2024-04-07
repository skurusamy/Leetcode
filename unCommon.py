str1 = "characters"
str2 = "alphabets"
val = set()
ans = ""
for i in str1:
    if i not in str2:
        val.add(i)
for j in str2:
    if j not in str1:
        val.add(j)
print(sorted(val))
for i in sorted(val):
    ans += i
print(ans)
'''
for i in range(len(str1)):
    if str1[i] not in val:
        val.add(str1[i])
for i in range(len(str2)):
    if str2[i] not in val:
        ans += str2[i]
print(ans)
'''