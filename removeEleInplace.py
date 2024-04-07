Arr = [1,1,2,3,4,5,1]
num = 2
index=0
for i in range(len(Arr)):
    if Arr[i] != num:
        Arr[index] = Arr[i]
        index += 1
print(index)
print(Arr)