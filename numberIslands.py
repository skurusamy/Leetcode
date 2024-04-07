def numIslands(grid, i, j):
        """
        :type grid: List[List[str]]
        :rtype: int
        """
        if i < 0 or j < 0 or i >= len(grid) or j >= len(grid[i]) or grid[i][j] == '0':
            return 0
        grid[i][j] = '0'
        numIslands(grid, i + 1, j)
        numIslands(grid, i - 1, j)
        numIslands(grid, i, j + 1)
        numIslands(grid, i, j - 1)
        return 1
'''
grid = [
  ["1","1","1","1","0"],
  ["1","1","0","1","0"],
  ["1","1","0","0","0"],
  ["0","0","0","0","0"]
]
'''
grid = [['1', '1', '0'], ['0', '0', '1'], ['0', '1', '0']]
count = 0
for i in range(len(grid)):
    for j in range(len(grid[i])):
        if grid[i][j] == '1':
            count += numIslands(grid,i,j)
print(count)