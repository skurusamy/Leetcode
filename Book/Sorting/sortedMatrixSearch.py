def search(arr,key):
    row = 0
    #rowEnd = len(arr)
    #colstart = 0
    col = len(arr[0]) -1
    while(row < len(arr) and col >= 0):
        if key == arr[row][col]:
            return True
        if key > arr[row][col]:
            row += 1
        else:
            col -= 1
    return False

#arr = [[1,2,3,4],[5,6,7,8],[9,10,11,12],[13,14,15,16]]
arr = [[15,20,70,85],[25,35,80,95],[30,55,95,105],[40,80,100.120]]
key = 50
print(search(arr,key))