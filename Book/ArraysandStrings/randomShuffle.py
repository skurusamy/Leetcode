import random
arr = [2,3,1,4,5,10]
pos = set()
while True:
    i = random.randrange(0,len(arr))
    j = random.randrange(0,len(arr))
    if i not in pos and j not in pos:
        arr[i],arr[j] = arr[j],arr[i]
        pos.add(i)
        pos.add(j)
    if len(pos)  == len(arr):
        break
print(arr)