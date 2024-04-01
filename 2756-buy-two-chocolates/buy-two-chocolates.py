class Solution:
    def buyChoco(self, prices: List[int], money: int) -> int:
        min_ = 101
        secondMin = 101
        for price in prices:
            if price <= min_ :
                secondMin = min_
                min_ = price
            elif price < secondMin and price > min_ :
                secondMin = price
        totalCost = min_ + secondMin
        if totalCost > money:
            return money
        else:
            return money-totalCost
        

