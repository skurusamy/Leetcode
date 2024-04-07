s = "leetcode"
dic = {}
for i in s:
    if i in dic:
        dic[i] += 1
    else:
        dic[i]  = 1
for i in s:
    if dic[i] == 1:
        print(s.index(i))
        break   