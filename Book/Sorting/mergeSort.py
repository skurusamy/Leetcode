def mergeSort(arr):
    if len(arr) <=1:
        return
    mid = (len(arr)) // 2
    left = arr[:mid]
    right = arr[mid:]
    mergeSort(left)
    mergeSort(right)
    merge(arr,left,right)

def merge(arr,left,right):
    i = 0 
    k = 0
    j = 0
    while i< len(left) and j < len(right):
        if left[i] <= right[j]:
            arr[k] = left[i]
            i += 1
        else:
            arr[k] = right[j]
            j += 1
        k += 1
    while i < len(left) :
        arr[k] = left[i]
        i += 1
        k += 1
    while j < len(right):
        arr[k] = right[j]
        j += 1
        k += 1
    return


arr = [100,50,80,10,1,23,126]
print(arr)
mergeSort(arr)
print(arr)