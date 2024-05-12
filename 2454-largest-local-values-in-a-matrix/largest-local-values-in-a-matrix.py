class Solution:
    def largestLocal(self, grid: List[List[int]]) -> List[List[int]]:
        n = len(grid)
        # topMostSide = grid[0][0:(n-2)]
        # leftMostSide = grid[0:(n-2)][0] 
        res = []
        for i in range(1, n-1):
            newRow = []
            for j in range(1, n-1):
                currVal = max([grid[i-1][j-1], grid[i-1][j], grid[i-1][j+1], 
                grid[i][j-1], grid[i][j], grid[i][j+1],
                grid[i+1][j-1], grid[i+1][j], grid[i+1][j+1]])
                newRow.append(currVal)
            res.append(newRow)
        return res

