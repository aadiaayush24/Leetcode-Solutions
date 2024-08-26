class Solution:
    def check(self, nums: List[int]) -> bool:
        once =True
        last = nums[0]
        for x in nums[1:]:
            if x < last:
                if once:
                    once = False
                else:
                    return False
            last = x
        if not once:
            if nums[0] >= nums[-1]:
                return True
            return False
        return True