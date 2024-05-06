class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        stack = []
        maxProfit = 0
        for p in prices[::-1]:
            if not stack:
                stack.append(p)
            else:
                if p > stack[-1]:
                    stack.append(p)
                else:
                    currProfit = stack[-1]-p
                    if maxProfit < currProfit:
                        maxProfit = currProfit
        return maxProfit