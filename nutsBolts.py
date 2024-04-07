nuts = ['@', '#', '$', '%', '^', '&']
bolts = ['$', '%', '&', '^', '@', '#']
order = ['!', '#', '$', '%', '&', '*' ,'@', '^', '~']
dic={}
for i in range(len(nuts)):
    if nuts[i] not in dic:
        dic[nuts[i]]=i
for i in range(len(nuts)):
    if bolts[i] in dic:
        nuts[i] = bolts[i]
print("nuts: ")
for i in order:
    if i in nuts:
        print(i,end=" ")
print("\nbolts: ")
for i in order:
    if i in bolts:
        print(i,end=" ")