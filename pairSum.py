Arr = [1,2,3,4,3,5,2,0]
target = 4
'''
Arr.sort()
low = 0
high = len(Arr)-1
while low < high:
    if Arr[low]+Arr[high] == target:
        print(str(Arr[low])+" "+str(Arr[high]))
    if Arr[low] + Arr[high] > target:
        high -= 1
    else:
        low += 1
'''
s =set()
pos=set()
for i in range(len(Arr)):
    val = target - Arr[i]
    if val in Arr and (i not in pos or Arr.index(val) not in pos):
        print("Value",Arr[i],val)
        print("Pos",i,Arr.index(val))
        pos.add(i)
        pos.add(Arr.index(val))
