nums = [1,2,2,3,3,3]
dic = {}
lucky_val = -1
for i in nums:
    dic[i]  = 1 + dic.get(i,0)
for k in dic.keys():
    if dic[k] == k:
        lucky_val = max(lucky_val,k)
print(lucky_val)
