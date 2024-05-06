class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        n = len(matrix[0])
        m = len(matrix)
        zeroIndices = []
        for i in range(m):
            for j in range(n):
                if matrix[i][j] == 0:
                    zeroIndices.append((i,j))
        for x, y in zeroIndices:
            for i in range(0, n):
                matrix[x][i] = 0
            for j in range(0, m):
                matrix[j][y] = 0
        