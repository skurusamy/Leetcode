# n square solution
'''
arr = [1,2,3,4,5,1]
target = 3
count = 0
for i in range(len(arr)):
    for j in range(i+1,len(arr)):
        if arr[i] + arr[j] == target:
            count += 1
print(count)
'''
'''
# n solution

arr = [1,2,3,4,5,1,0]
target = 3
count = {}
pairs=0
for i in arr:
    if i in count:
        count[i] += 1
    else:
        count[i] = 1
for i in range(len(arr)):
    print(count)
    val = target - arr[i]
    if val in count:
        pairs += count[val]
    if arr[i] == val:
        pairs -= 1
print(pairs//2)
'''
#nlogn
arr = [1,2,3,4,5,1,0,3]
target = 3
arr.sort()
i = count = 0
j = len(arr)-1
while j >= i:
        val = target - arr[i]
        if val < arr[j]:
            j -= 1
        elif val > arr[j]:
            i += 1
        else:
            count += 1
            j -= 1
print(count)