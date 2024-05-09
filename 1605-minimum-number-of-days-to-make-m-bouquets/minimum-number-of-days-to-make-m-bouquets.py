class Solution:
    def minDays(self, bloomDay: List[int], m: int, k: int) -> int:
        def checkBouquetPossible(n: int):
            bouquet = 0
            adjFlowers = 0
            for b in bloomDay:
                if b <= n:
                    adjFlowers += 1
                    if adjFlowers == k:
                        adjFlowers = 0
                        bouquet += 1
                        if bouquet == m:
                            return True
                else:
                    adjFlowers = 0
            return False
        
        start, end = 1, max(bloomDay)
        if len(bloomDay) < (m*k):
            return -1
        while (start < end):
            mid = start + (end - start)//2
            if checkBouquetPossible(mid):
                end = mid
            else:
                start = mid + 1
        return start 