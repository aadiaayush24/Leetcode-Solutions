class Solution:
    def lemonadeChange(self, bills: List[int]) -> bool:
        def change(cash, target):
            for denom in [20, 10, 5]:
                if (target >= denom and cash[denom] > 0):
                    x = target//denom if target//denom <= cash[denom] else cash[denom]
                    cash[denom] -= x
                    target = target - (x*denom)
            if target == 0:
                return True
            else:
                return False
        cash = {5: 0, 10: 0, 20: 0}
        for bill in bills:
            target = bill - 5
            if target != 0:      
                if not cash:
                    return False
                if not change(cash, target):
                    return False
            cash[bill] += 1
            print(cash)
        return True
            
            
        