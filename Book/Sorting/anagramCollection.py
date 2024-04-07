from collections import defaultdict
arr =  ["cat","tac","dog","go","og"]
dic = defaultdict(list)
for i in arr:
    ans ="".join(sorted(i))
    dic[ans].append(i)
print(dic.values())


