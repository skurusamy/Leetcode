nums = [2,4,5,6,2,5,2,1,4]
dic = {}
for num in nums:
    dic[num] = 1 + dic.get(num,0)


for key, val in dic.items():
    print(key, val)

new_dic = sorted(dic.items(), key = lambda x : (x[1],x[0]))
print(new_dic)