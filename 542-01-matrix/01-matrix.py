class Solution:
    def updateMatrix(self, matrix: List[List[int]]) -> List[List[int]]:
        m = len(matrix)
        n = len(matrix[0])
        dist = [[-1 for j in range(n)] for i in range(m)]
        queue = deque()
        for i in range(m):
            for j in range(n):
                if matrix[i][j] == 0:
                    queue.append((i, j, 0))
                    dist[i][j] = 0
        dirs = [(-1, 0), (1, 0), (0, -1), (0, 1)]
        while (queue):
            x, y, steps = queue.popleft()
            for dx, dy in dirs:
                nx = x+dx
                ny = y+dy
                if (0 <= nx < m) and (0 <= ny < n):
                    if dist[nx][ny] == -1:
                        dist[nx][ny] = steps+1
                        queue.append((nx, ny, steps+1))
        return dist
