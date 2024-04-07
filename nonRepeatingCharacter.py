import sys
s = 'loveleetcode'
min = -1
dic = {}
for i in range(len(s)):
    if s[i] not in dic:
        dic[s[i]] = i
    else:
        dic[s[i]] = -1
for i in dic.keys():
    if dic[i] != -1 and dic[i] < min:
        min = dic[i]
print("The least index of non repeating character is ", min)
