class Solution:
    def findKthPositive(self, arr: List[int], k: int) -> int:
        start = 0
        end = len(arr) - 1
        while (start <= end):
            mid = start + (end-start)//2
            count_missing = arr[mid] - mid - 1
            if count_missing < k:
                start = mid + 1
            else:
                end = mid - 1
        return start + k