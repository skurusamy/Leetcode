'''
Find occurence of a particular element in an array
'''
arr = [1,3,3,4,6,7,8,2,1,3,5]
ele = -1
dic ={}
for i in arr:
    if i not in dic:
        dic[i] = 1
    else:
        dic[i] += 1
if ele in dic:
    print(dic[ele])
else:
    print(0)