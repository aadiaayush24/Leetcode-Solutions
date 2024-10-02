class Solution:
    def myPow(self, x: float, n: int) -> float:
        def power(x, n):
            if n == 0:
                return 1
            tmp = power(x, n//2)
            res = tmp * tmp
            if (n%2 == 1):
                res *= x
            return res
        if n < 0:
            n *= -1
            x = 1/x
        elif n == 0:
            return 1
        return power(x, n) 
                
        