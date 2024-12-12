from collections import deque
class Solution:
    def numEnclaves(self, grid: List[List[int]]) -> int:
        def doBfs(i, j):
            queue = deque()
            dirs = [(-1, 0), (1, 0), (0, -1), (0, 1)]
            queue.append ((i, j))
            vis[i][j] = True
            count = 0
            while (queue):
                x, y = queue.popleft()
                count += 1
                for dx, dy in dirs:
                    nx = x + dx
                    ny = y + dy
                    if (0 <= nx < m and 0 <= ny < n and grid[nx][ny] == 1 and not vis[nx][ny]):
                        vis[nx][ny] = True
                        queue.append((nx, ny))
            return count
        
        m = len(grid)
        n = len(grid[0])
        vis = [[False for j in range(n)] for i in range(m)]
        total_ones = 0
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 1:
                    total_ones += 1
        
        reachable_ones = 0
        for j in range(n):
            if (grid[0][j] == 1) and not (vis[0][j]):
                reachable_ones += doBfs(0, j)
            if (m > 1):
                if (grid[m-1][j] == 1) and not (vis[m-1][j]):
                    reachable_ones += doBfs(m-1, j)
            
        for i in range(1, m-1):
            if (grid[i][0] == 1) and not (vis[i][0]):
                reachable_ones += doBfs(i, 0)
            if (n > 1):
                if (grid[i][n-1] == 1) and not (vis[i][n-1]):
                    reachable_ones += doBfs(i, n-1)
        
        return total_ones - reachable_ones
        
            
