'''
Sort the array of 0s 1s and 2s
'''
arr = [0, 1, 2, 0, 1, 0]
out = []
dic ={}
for i in arr:
    if i not in dic:
        dic[i] = 1
    else:
        dic[i] += 1
i=0
while dic[0] > 0:
    arr[i] = 0
    i +=1
    dic[0] -= 1
while dic[1] > 0:
    arr[i] = 1
    i +=1
    dic[1] -= 1
while dic[2] > 0:
    arr[i] = 2
    i +=1
    dic[2] -= 1
print(arr)