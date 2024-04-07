def numOfIslands(grid, i, j):
    if i < 0 or i>=len(grid) or j < 0 or j >= len(grid[0]) or grid[i][j] == '0':
        return 0
    grid[i][j] = '0'
    numOfIslands(grid, i+1, j)
    numOfIslands(grid, i, j+1)
    numOfIslands(grid, i-1, j)
    numOfIslands(grid, i, j-1)
    return 1
grid = [
  ["1","1","0","0","0"],
  ["1","1","0","0","0"],
  ["0","0","1","0","0"],
  ["0","0","0","1","1"]
]   
ans = 0
for i in range(len(grid)):
    for j in range(len(grid[0])):
        ans += numOfIslands(grid,i, j)
print(ans)