class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        m = len(grid)
        n = len(grid[0])
        dp = [[-1] * n for _ in range(m)]
        dp[0][0] = grid[0][0]
        def fillDP(i, j):
            if (0<=i<m and 0<=j<n):
                if dp[i][j] == -1:
                    dp[i][j] = grid[i][j] + min(fillDP(i-1, j), fillDP(i, j-1))
                return dp[i][j]
            else:
                return float('inf')
        return fillDP(m-1, n-1) 
        