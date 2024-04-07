
def dfs(grid,i,j):
    if i < 0 or j<0 or i >= len(grid) or j >= len(grid[0]) or grid[i][j]!=1:
        return 0
    grid[i][j]= 0
    count = 1
    count += dfs(grid,i+1,j)
    count += dfs(grid, i - 1, j)
    count += dfs(grid, i , j+1)
    count += dfs(grid, i , j-1)
    return count

def maxArea(grid):
    maxi = 0
    for i in range(len(grid)):
       for j in range(len(grid[0])):
           if grid[i][j]==1:
                maxi = max(maxi,dfs(grid,i,j))
    return maxi


grid = [[0,0,1,0,0,0,0,1,0,0,0,0,0],
 [0,0,0,0,0,0,0,1,1,1,0,0,0],
 [0,1,1,0,1,0,0,0,0,0,0,0,0],
 [0,1,0,0,1,1,0,0,1,0,1,0,0],
 [0,1,0,0,1,1,0,0,1,1,1,0,0],
 [0,0,0,0,0,0,0,0,0,0,1,0,0],
 [0,0,0,0,0,0,0,1,1,1,0,0,0],
 [0,0,0,0,0,0,0,1,1,0,0,0,0]]
print(maxArea(grid))