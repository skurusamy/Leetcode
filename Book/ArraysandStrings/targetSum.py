arr = [1,5,3,2,0,4]
target = 4
dic = {}
for i in arr:
    if i not in dic:
        dic[i] = 1
    else:
        dic[i] += 1
count =0
for i in range(len(arr)):
    secondval  = target - arr[i]
    if secondval in dic:
        count += dic[secondval]
    if secondval == arr[i]:
        count = count - 1
print(count//2)
