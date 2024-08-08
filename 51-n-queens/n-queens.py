class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        def eliminate(x, y, n):
            notAllowed = set()
            # For row - i = x, 0 <= j < n
            # For col - j = y, 0 <= i < n
            for r in range(0, n):
                notAllowed.add((x, r))
                notAllowed.add((r, y))

            # For upper-diagonal x<i<n, y<j<n
            i, j = x, y
            while (i < n and j < n):
                notAllowed.add((i, j))
                i += 1
                j += 1

            # For lower-diagonal 0<=i<x, 0<=j<y
            i, j = x, y
            while (i >=0 and j>= 0):
                notAllowed.add((i, j))
                i -= 1
                j -= 1


            # For upper-opposite diagonal i < n and j >= 0
            i, j = x, y
            while (i < n and j >= 0):
                notAllowed.add((i, j))
                i += 1
                j -= 1


            # For lower-opposite diagonal j < n and i >= 0
            i, j = x, y
            while (j < n and i >= 0):
                notAllowed.add((i, j))
                j += 1
                i -= 1
            return notAllowed

        def findBoard(queens, notAllowed, row):
            if row == n:
                res.append(queens[:])
                return
            for col in range(n):
                if (row, col) not in notAllowed:
                    nextNotAllowed = eliminate(row, col, n)
                    queens.append((row, col))
                    findBoard(queens, notAllowed | nextNotAllowed, row+1)
                    queens.pop()
            return
        res = []
        findBoard([],set(), 0)
        boards = []
        for sol in res:
            board = []
            for i in range(n):
                row = ""
                for j in range(n):
                    if (i, j) in sol:
                        row += 'Q'
                    else:
                        row += '.'
                board.append(row)
            boards.append(board[:])
        return boards 
            

            