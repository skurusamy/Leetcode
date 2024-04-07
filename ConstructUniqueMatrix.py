'''
Construct unique matrix
Input : n = 5
Output : 5 3 2 4 1 
         1 4 3 5 2 
         2 5 4 1 3 
         3 1 5 2 4 
         4 2 1 3 5 

'''
n = 5
arr = [[0 for i in range(n)] for j in range(n)]
left = 0
right = n-1

#fill one's ---
## starting from right in first row, then left, then right and so on
for i in range(n): # iterating each row
    if(i % 2 == 0): # start from right in first row
        arr[i][right] = 1
        j = right
        right -= 1
    else:
        arr[i][left] = 1
        j = left
        left += 1
    # filling other vales other than 1
    row = i+1
    fill_val = 2
    loopCount =1
    while(loopCount < n):
        arr[row % n][j] = fill_val
        fill_val += 1
        row = (row+1) % n
        loopCount += 1
for i in range(n):
    for j in range(n):
        print(arr[i][j],end=" ")
    print()