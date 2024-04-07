'''
https://www.youtube.com/watch?v=t_TMt_BFGiQ

'''
arr = [3,2,8,4,1]
i = len(arr)-2
while i > 0:
    if arr[i+1] < arr[i]:
        i -= 1
    else:
        break
d1 = arr[i]
print("d1",d1)
small = -99999
small_index = 0
for  j in range(i+1,len(arr)):
    if d1 > arr[j] and small < arr[j]:
        small =arr[j]
        small_index = j
arr[i],arr[small_index] = arr[small_index],arr[i]

print(arr)
print(arr[0:i+1]+sorted(arr[i+1:len(arr)]))