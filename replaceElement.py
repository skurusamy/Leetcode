def replaceElements( arr) :
        max = arr[len(arr) - 1]
        arr[len(arr)-1] = -1
        for i in range(len(arr)-2,-1,-1):
            if arr[i] > max:
                temp = arr[i]
                arr[i] = max
                max = temp
            else:
                    arr[i] = max
        return arr

print(replaceElements([17,18,5,4,6,1]))