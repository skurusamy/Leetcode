def getMaximumGold( grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        def dfs(grid,i,j):
            if i < 0 or i >= len(grid) or j < 0 or j>= len(grid[0]) or grid[i][j] == 0:
                return 0
            temp = grid[i][j]
            grid[i][j] = 0
            
            right = dfs(grid,i , j-1)
            down = dfs(grid,i,j+1)
            left = dfs(grid,i-1,j)
            top = dfs(grid,i+1,j)
            grid[i][j] = temp
            ans = max(left,top,down,right) + temp
            return ans
        maxi = 0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] != 0:
                    ans = dfs(grid,i,j)
                    if ans> maxi:
                        maxi = ans
        return maxi
grid = [[0,6,0],[5,8,7],[0,9,0]]
print(getMaximumGold(grid))