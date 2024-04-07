arr = [2,3,1,2,3,4,0]
pos =set()
target = 4
for i in arr:
    val = target - i
    if val in arr and (arr.index(i) not in pos or arr.index(val) not in pos):
        print(i,val)
        pos.add(arr.index(i))
        pos.add(arr.index(val))
