'''
In a given  array - return the index of peak element - which is greater than its neighbours
'''

arr = [1,2,3,1]
#arr = [1,2,1,3,5,6,4]
#naive solution complexity O(n)
'''

peakIndex = -1
for i in range(1,len(arr)-1):
    if(arr[i] > arr[i+1] and arr[i] > arr[i-1]):
        peakIndex = i
print(peakIndex)
'''

#binary search solution complexity O(log n)

left = 0
right = len(arr)-1
while(left < right):
    mid = (right + left) // 2
    if(arr[mid] < arr[mid+1]):
        left = mid + 1
    else:
        right = mid
print(left)