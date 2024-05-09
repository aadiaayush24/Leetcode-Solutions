import math
class Solution:
    def smallestDivisor(self, nums: List[int], threshold: int) -> int:
        def isLessThanOrEqualToThreshold (divisor: int):
            result = sum(int(math.ceil(num/divisor)) for num in nums)
            return result <= threshold
        
        start, end = 1, max(nums)
        while (start < end):
            mid = start + (end - start)//2
            if isLessThanOrEqualToThreshold(mid):
                end = mid
            else:
                start = mid + 1
        return start