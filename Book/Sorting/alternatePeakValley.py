def maxi(a,b,c):
    if a > b and a> c: return a
    elif b>c : return b
    else: return c

arr = [5,3,1,2,3]

'''
Sort and swap
'''
arr = sorted(arr)
for i in range(0,len(arr)-1,2):
    arr[i],arr[i+1] = arr[i+1],arr[i]
print(arr)

'''
without sorting, find max of 3 elements and swap with neighbor
'''


for i in range(0,len(arr)-1,2):
    peak = maxi(arr[i],arr[i-1],arr[i+1])
    if peak != arr[i]:
        arr[i],arr[i-1] = arr[i-1],arr[i]
print(arr)