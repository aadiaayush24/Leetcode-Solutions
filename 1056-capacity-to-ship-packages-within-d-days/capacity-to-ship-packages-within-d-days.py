class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:
        def checkKWeightAllowsAll(k: int):
            day = 1
            currentTotalWeight = 0
            i = 0
            for w in weights:
                if ((currentTotalWeight + w) <= k):
                    currentTotalWeight += w
                else:
                    day += 1
                    if w > k:
                        return False
                    currentTotalWeight = w
                if (day > days):
                    return False
            return True

        start = 1
        end = sum(weights)

        while (start < end):
            mid = start + (end - start)//2
            if checkKWeightAllowsAll(mid):
                end = mid
            else:
                start = mid + 1
        return start
