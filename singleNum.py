arr = [2,2,1,1,3]
dic =set()
for i in arr:
    if i in dic:
        dic.remove(i)
    else:
        dic.add(i)
for i in dic:
    print(i)