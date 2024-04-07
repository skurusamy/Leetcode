st1 = "bbale"
st2 = "pbal"
dic = {}
for i in st1:
    if i not in dic:
        dic[i] = 1
    else:
        dic[i] += 1
for i in st2:
    if i in dic:
        dic[i] -= 1
    else:
        dic[i] = 1
print(dic)
count = sum(dic.values())
'''
for i in dic.keys():
    if dic[i] != 0:
        count += dic[i]
print(dic)
'''
if count == 0 or count == 1 or count == 2:
    print("yes")
else:
    print("No")