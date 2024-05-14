class Solution:
    def getMaximumGold(self, grid: List[List[int]]) -> int:
        def dfs(i, j):
            if (i < 0 or i >= n or j < 0 or j >= m or grid[i][j] == 0):
                return 0
            
            currGold = grid[i][j]
            grid[i][j] = 0
            maxGold = 0
            dirs = ((1, 0), (0, 1), (-1, 0), (0, -1))
            for i_, j_ in dirs:
                x = i + i_
                y = j + j_
                maxGold = max(maxGold, currGold+dfs(x, y))
            grid[i][j] = currGold
            return maxGold
        
        n = len(grid)
        m = len(grid[0])
        maxGold = 0
        for i in range(n):
            for j in range(m):
                if grid[i][j] != 0:
                    maxGold = max(maxGold, dfs(i, j))
        return maxGold
