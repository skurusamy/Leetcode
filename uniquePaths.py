rows = int(input("Enter the rows: "))
cols = int(input("Enter the column: "))
rid = [[1]*cols for i in range(rows)]
for i in range(1,rows):
    for j in range(1,cols):
        rid[i][j] = rid[i-1][j] + rid[i][j-1]
print(rid[rows-1][cols-1])