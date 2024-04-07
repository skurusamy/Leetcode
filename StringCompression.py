''''
arr =['a','a','a','b','b']
output =['a','3','b','2'] = 4

arr = [a]
output = 1 = [a]
'''

arr = ['a','a','b','b','c','c','c','c']
index = 0
i =0
while i < len(arr):
    j = i
    while j < len(arr) and arr[i] == arr[j]:
        j += 1
    if j-i > 1:
        arr[index] = arr[i]
        index += 1
        arr[index] = str(j-i)
        index += 1
    i = j
print(arr, index)