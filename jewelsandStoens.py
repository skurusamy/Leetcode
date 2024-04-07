j = "aA"
s = "aAAAbb"
dic = {}
for i in s:
    if i not in dic:
        dic[i] = 1
    else:
        dic[i] += 1
count = 0
for i in j:
    if i in dic.keys():
        count += dic[i]
print(count)
