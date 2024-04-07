rows = int(input("Enter rows: "))
col = int(input("Enter col: "))
mat =[]
max_ind = 0
for i in range(rows):
    colu=[]
    for j in range(col):
        colu.append(int(input()))
    mat.append(colu)
# find first 1 in row1
for i in mat[0]:
    if i ==1:
        ind =i
        break
if ind == -1:
    ind = col -1
for i in range(1,rows):
    while ind >= 0 and mat[i][ind] == 1:
        ind = ind - 1
        max_ind = i
print(mat)
print(max_ind)