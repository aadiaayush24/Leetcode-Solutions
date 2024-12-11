from collections import deque
class Solution:

    def numIslands(self, grid: List[List[str]]) -> int:
        def doBfs(i, j):
            visited[i][j] = True
            queue = deque()
            dirs = [(0, 1), (0, -1), (1, 0), (-1, 0)]
            queue.append((i, j))
            while (queue):
                i, j = queue.popleft()
                for dx, dy in dirs:
                    nx = i + dx
                    ny = j + dy
                    if (0 <= nx < m) and (0 <= ny < n) and (not visited[nx][ny]) and (grid[nx][ny] == '1'):
                        visited[nx][ny] = True
                        queue.append((nx, ny))
            return
        
        m = len(grid)
        n = len(grid[0])
        cntIslands = 0
        visited = [[False for j in range(n)] for i in range(m)]
        for i in range(m):
            for j in range(n):
                if (not visited[i][j]) and (grid[i][j] == '1'):
                    cntIslands += 1
                    doBfs(i, j)
        return cntIslands

                



