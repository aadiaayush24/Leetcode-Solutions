class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        dp = {}
        def findMaxProfit(index, canBuy):
            if (index, canBuy) in dp.keys():
                return dp[(index, canBuy)]
            if index >= len(prices):
                return 0
            else:
                if canBuy:
                    dp[(index, canBuy)] = max(-prices[index] + findMaxProfit(index+1, False), 0+findMaxProfit(index+1, True))
                else:
                    dp[(index, canBuy)] = max(prices[index] + findMaxProfit(index+2, True), 0+findMaxProfit(index+1, False))
                return dp[(index, canBuy)]
        
        res = findMaxProfit(0, True)
        return res if res > 0 else 0