class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        tri = [[1]]
        def fillTri(prevRow: list, n: int):
            if n == numRows:
                return
            newRow = [1]
            prev = 1
            for x in prevRow[1:len(prevRow)]:
                newRow.append(prev+x)
                prev = x
            newRow.append(1)
            tri.append(newRow)
            fillTri(newRow[:], n+1)
        fillTri([1], 1)
        return tri
