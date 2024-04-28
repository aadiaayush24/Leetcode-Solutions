class Solution:
    def maxProfit(self, prices: List[int], fee: int) -> int:
        dp = {}
        def findMaxProfit(index, buy):
            if (index, buy) in dp.keys():
                return dp[(index, buy)]
            if index == len(prices):
                return 0
            else:
                if buy:
                    dp[(index, buy)] = max(-prices[index]+findMaxProfit(index+1, False), 0+findMaxProfit(index+1, True))
                else:
                    dp[(index, buy)] = max(prices[index] - fee + findMaxProfit(index+1, True), 0 + findMaxProfit(index+1, False))
                return dp[(index, buy)]
        return findMaxProfit(0, True)