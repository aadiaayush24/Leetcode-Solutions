class Solution:
    def mincostToHireWorkers(self, quality: List[int], wage: List[int], k: int) -> float:
        """
        Input: quality = [10,20,5], wage = [70,50,30], k = 2

        quality/wage = [1/7, 2/5, 1/6]
        sorted()       [1/7, 1/6, 2/5]
        quality =      [10, 5, 20]
        
        store k-workers rate in max-heap (the quality of k workers which ask least amount)
        """
        rate = sorted(zip(quality, wage), key = lambda x: x[1]/x[0])
        maxHeap = []
        n = len(rate)
        total_quality = 0
        bestWage = float('inf')
        for i in range(n):
            total_quality += rate[i][0]
            heapq.heappush(maxHeap, -rate[i][0])

            if len(maxHeap) > k:
                top = -heapq.heappop(maxHeap)
                total_quality -= top
            
            if len(maxHeap) == k:
                cost = total_quality * (rate[i][1]/rate[i][0])
                bestWage = min(cost, bestWage)
            
        return bestWage
            



