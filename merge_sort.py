def mergeSort(arr):
    if len(arr)>1:
        mid = len(arr)//2
        left = arr[:mid]
        right = arr[mid:]
        mergeSort(left)
        mergeSort(right)

        i = 0
        j = 0
        k = 0
        while i < len(left) and j < len(right):
            if left[i] <= right[j]:
              arr[k] = left[i]
              i += 1
            else:
                arr[k] = right[j]
                j += 1
            k += 1
        while i < len(left):
            arr[k] = left[i]
            k += 1
            i += 1
        while j < len(right):
           arr[k] = right[j]
           k += 1
           j += 1
        print(arr)
        return


# main
n = int(input("Size of an array: "))
arr = []
print(n)
for o in range(n):
    arr.append(int(input()))
mergeSort(arr)
print(arr)
