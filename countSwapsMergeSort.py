def mergeSort(arr,left,right,temp_arr):
    count = 0
    if left < right:
        mid = (left+right)//2
        count += mergeSort(arr,left,mid,temp_arr)
        count += mergeSort(arr,mid+1,right,temp_arr)
        count += merge(arr,left,mid,right,temp_arr)
    return count
def merge(arr,left,mid,right,temp_arr):
    count = 0
    i = left
    j = mid+1
    k = left
    while i <= mid and j <= right:
        if arr[i] <= arr[j]:
            temp_arr[k] = arr[i]
            i += 1
        else:
            temp_arr[k] = arr[j]
            count += (mid - i + 1)
            j += 1
        k += 1
    while i <= mid:
        temp_arr[k] = arr[i]
        k += 1
        i += 1
    while j <= right:
        temp_arr[k] = arr[j]
        k += 1
        j += 1
    return count


n = int(input("Enter n: "))
arr = []
for i in range(n):
    arr.append(int(input()))
temp_arr = [0]*n
count = mergeSort(arr,0,n-1,temp_arr)
print(count)