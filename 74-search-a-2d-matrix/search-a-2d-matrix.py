class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        def binary_search(arr, val):
            start = 0
            end = len(arr)-1
            res = -1
            while (start <= end):
                mid = start + (end - start)//2
                if (arr[mid] == val):
                    return mid
                elif (arr[mid] < val):
                    res = mid
                    start = mid + 1
                else:
                    end = mid - 1
            return res
        firstNumOfEachRow = [row[0] for row in matrix]
        rowNum = binary_search(firstNumOfEachRow, target)
        if rowNum < 0:
            rowNum = 0
        colNum = binary_search(matrix[rowNum], target)
        print(colNum, matrix[rowNum][colNum])
        if matrix[rowNum][colNum] == target:
            return True
        else:
            return False
        