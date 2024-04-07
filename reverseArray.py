arr = [2,3,4,6,1,5]
# o(n)
'''
for i in range(len(arr)-1,-1,-1):
    print(arr[i],end =',')
'''
#O(logn)
start = 0
end = len(arr)-1
while start < end:
    temp = arr[start]
    arr[start] = arr[end]
    arr[end] = temp
    start += 1
    end -= 1
print(arr)
