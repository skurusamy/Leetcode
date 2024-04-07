def search(arr,key,left,right):
    if left > right:
        return -1

    mid = (right + left ) // 2
    if arr[mid]=="": # find nearest non empty string
        leftnonEmpty = mid -1
        rightnonEmpty = mid +1 
        while True:
            if leftnonEmpty < left and rightnonEmpty > right: # beyomd the boundry
                return -1
            if leftnonEmpty > left and arr[leftnonEmpty] != "":
                mid = leftnonEmpty
                break
            if rightnonEmpty < right and arr[rightnonEmpty] != "":
                mid = rightnonEmpty
                break
    if key == arr[mid]:
        return mid
    if key < arr[mid]:
        return search(arr,key,left,mid)
    else:
        return search(arr,key,mid+1,right)


arr = ["at","","","ball","","","cat","","","dad",""]
print(search(arr,"ball",0,len(arr)))