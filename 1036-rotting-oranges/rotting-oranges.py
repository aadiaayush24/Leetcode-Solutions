from collections import deque
class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        queue = deque()
        m = len(grid)
        n = len(grid[0])
        level = 0
        for row in range(m):
            for col in range(n):
                if (grid[row][col] == 2):
                    queue.append((row, col, level))
        dirs = [(-1, 0), (1, 0), (0, -1), (0, 1)]

        while (queue):
            r, c, l = queue.popleft()
            level = max(level, l)
            for x, y in dirs:
                if ((0<=(r+x) < m) and (0 <= (c+y) <n) and (grid[r+x][c+y] == 1)):
                    grid[r+x][c+y] = 2
                    queue.append((r+x, c+y, l+1))
        for row in grid:
            if 1 in row:
                return -1
        return level




        



