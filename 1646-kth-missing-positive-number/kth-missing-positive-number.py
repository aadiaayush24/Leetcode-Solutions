class Solution:
    def findKthPositive(self, arr: List[int], k: int) -> int:
        def found(x):
            start = 0
            end = len(arr)-1

            while (start <= end):
                mid = start + (end-start)//2
                if arr[mid] == x:
                    return True
                elif arr[mid] < x:
                    start = mid + 1
                else:
                    end = mid - 1
            return False
        
        number = 1
        countMissing = 0
        while (countMissing != k):
            if not found(number):
                countMissing += 1
            number += 1
        return number-1
