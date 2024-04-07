rows = int(input("Enter the number of rows: "))
col = int(input("Enter the number of col: "))
arr = []
for i in range(rows):
    coln = []
    for j in range(col):
        coln.append(int(input()))
    arr.append(coln)
top, left = 0, 0
right = col -1
bottom = rows -1
while True:
    if left > right:
        break
    else:
        for i in range(left,right+1):
            print(arr[top][i])
        top += 1
    if top > bottom:
        break
    else:
        for i in range(top, bottom+1):
            print(arr[i][right])
        right -= 1
    if left > right:
        break
    else:
        for i in range(right,left-1,-1):
            print(arr[bottom][i])
        bottom -= 1
    if top >  bottom:
        break
    else:
        for i in range(bottom,top-1,-1):
            print(arr[i][left])
        left += 1
