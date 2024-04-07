def dfs(grid,i,j):
    if i<0 or j<0 or i>= len(grid) or i >= len(grid[0]) or grid[i][j] == 0:
        return 0
    count = 1
    grid[i][j] =0
    count += dfs(grid,i-1,j)
    count += dfs(grid,i+1,j)
    count += dfs(grid,i,j-1)
    count += dfs(grid,i,j+1)
    return count


grid = [[0,0,1,0,0,0,0,1,0,0,0,0,0],
 [0,0,0,0,0,0,0,1,1,1,0,0,0],
 [0,1,1,0,1,0,0,0,0,0,0,0,0],
 [0,1,0,0,1,1,0,0,1,0,1,0,0],
 [0,1,0,0,1,1,0,0,1,1,1,0,0],
 [0,0,0,0,0,0,0,0,0,0,1,0,0],
 [0,0,0,0,0,0,0,1,1,1,0,0,0],
 [0,0,0,0,0,0,0,1,1,0,0,0,0]]

maxi =0
for i in range(len(grid)):
    for j in range(len(grid[0])):
        if grid[i][j] == 1:
         maxi = max(maxi,dfs(grid,i,j))
print(maxi)