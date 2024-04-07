Arr = [1,2,3,4,5,2,0]
target = 5
dic = {}
for ele in Arr:
    if ele not in dic:
        dic[ele] = 1
    else:
        dic[ele] += 1
print(dic)
second_val = 0
for i in range(len(Arr)):
    val = target - Arr[i]
    if val != Arr[i] and val in dic:
        second_val += dic[val]
print(second_val // 2)
