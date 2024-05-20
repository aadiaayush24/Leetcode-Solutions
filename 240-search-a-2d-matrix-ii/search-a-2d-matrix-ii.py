class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        def binary_search(arr, val):
            start = 0
            end = len(arr)-1
            res = -1
            while (start <= end):
                mid = start + (end - start)//2
                if arr[mid] == val:
                    return mid
                elif (arr[mid] < val):
                    res = mid
                    start = mid+1
                else:
                    end = mid -1
            return res
        rowPos = binary_search([arr[0] for arr in matrix], target)
        # print([arr[0] for arr in matrix])
        # print(rowPos)
        i = 0
        while (i <= rowPos):
            if (matrix[i][-1] >= target):
                # print(matrix[i][:])
                col = binary_search(matrix[i][:], target)
                if (matrix[i][col] == target):
                    return True
            i += 1
        return False
