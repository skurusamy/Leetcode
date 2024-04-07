'''
if an element in a colum or row is zero, then the complete row and needs to be made zero
'''
def makeZeroRow(mat, i):
    for col in range(len(mat[0])):
        mat[i][col] = 0

    return mat
def makeZeroCol(mat,j):
        for row in range(len(mat)):
            mat[row][j] = 0   
        return mat

mat = [[1,2,0],[2,5,1],[9,9,1]]
print(mat)
row = [False]*len(mat)
col = [False]*len(mat[0])
for i in range(len(mat)):
    for j in range(len(mat[0])):
        if(mat[i][j]) == 0:
            row[i] = True
            col[j] = True

for i in range(len(mat[0])):
    if row[i] is True:
        mat = makeZeroRow(mat,i)
for j in range(len(mat)):
    if col[j] is True:
        mat = makeZeroRow(mat,i)
print(mat)