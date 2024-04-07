# https://www.geeksforgeeks.org/find-number-of-positional-elements/

'''
Input : a = {{1, 3, 4}, {5, 2, 9}, {8, 7, 6}} 
Output : 7 
'''
import sys
a = [[1,3,4],[5,2,9],[8,7,6]]
minRow = [sys.maxsize] * len(a)
minCol = [sys.maxsize] * len(a[0])
maxRow = [-sys.maxsize] * len(a)
maxCol = [-sys.maxsize] * len(a[0])

for i in range(len(a)):
    rmin,rmax = sys.maxsize,-sys.maxsize
    for j in range(len(a[0])):
        if rmin > a[i][j]:
            rmin = a[i][j]
        if rmax < a[i][j]:
            rmax = a[i][j]
    minRow[i] = rmin
    maxRow[i] = rmax


for j in range(len(a[0])):
    cmin,cmax = sys.maxsize,-sys.maxsize
    for i in range(len(a)):
        if cmin > a[i][j]:
            cmin = a[i][j]
        if cmax < a[i][j]:
            cmax = a[i][j]
    minCol[j] = cmin
    maxCol[j] = cmax

print(minRow,maxRow)
print(minCol,maxCol)
count =0
for i in range(len(a)):
    for j in range(len(a[0])):
        if a[i][j] == minRow[i] or a[i][j] == minCol[j] or a[i][j] == maxRow[i] or a[i][j] == maxCol[j]:
            count += 1
print(count)
