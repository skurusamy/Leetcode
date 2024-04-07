arr = [0,1,2,2,3,0,4,4]
target = 2
idx = 0
for i in arr:
    if i != target:
        arr[idx] = i
        idx += 1
print(idx)