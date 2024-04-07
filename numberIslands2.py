def numIslands2(grid, i, j):
    if i < 0 or j < 0 or i >= len(grid) or j >= len(grid[i]) or grid[i][j] == 0:
            return 0
    grid[i][j] = 0
    numIslands2(grid, i + 1, j)
    numIslands2(grid, i - 1, j)
    numIslands2(grid, i, j + 1)
    numIslands2(grid, i, j - 1)
    return 1



def formGrid(m,n,positions):
    if m == 0 or n == 0 or len(positions) == 0 :
        return None
    grid = [[0 for x in range(n)] for y in range(m)]
    for i in range(len(positions)):
        x,y = positions[i]
        grid[x][y] = 1
    return grid
            

m = 3
n = 3
positions = [[0,0],[0,1],[1,2],[2,1]]
grid = formGrid(m,n,positions)
print(grid)
if grid is None or len(grid) == 0:
    exit
islands = 0
output = []
for i in range(len(grid)):
    for j in range(len(grid[i])):
        if grid[i][j] == 1:
            islands += numIslands2(grid,i,j)
        for k in range(len(positions)):
            x,y = positions[k]
            if (x,y) == (i,j):  
                output.append(islands)
print(output)