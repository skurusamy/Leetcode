def display(mat):
    N = len(mat)
    for i in range(0, N):
         
        for j in range(0, N):
             
            print (mat[i][j], end = ' ')
        print ("")


#matrix = [[1,2,3,4],[5,6,7,-1],[8,9,0,-8],[-2,-3,-4,-5]]
matrix = [ [1, 2, 3, 4 ],
        [5, 6, 7, 8 ],
        [9, 10, 11, 12 ],
        [13, 14, 15, 16 ] ]

n = len(matrix)
display(matrix)
for i in range(len(matrix)):
    for j in range(i, n-i-1):
        temp = matrix[i][j]
        matrix[i][j] = matrix[j][n-1-i]
        matrix[j][n-1-i] = matrix[n-1-i][n-1-j]
        matrix[n-1-i][n-1-j] = matrix[n-1-j][i]
        matrix[n-1-j][i] = temp
print("---")
display(matrix)