arr = [5,1,4,4,9,7,13,3]
target = 3
dic ={}
for i in arr:
    if i not in dic:
        dic[i] = 1
    else:
        dic[i] += 1
rank = 0
for i in dic.keys():
    if i <= target:
        rank += dic[i]
print(rank-1)