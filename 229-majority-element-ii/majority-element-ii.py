class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        el1 = float('-inf')
        el2 = float('inf')
        c1 = 0
        c2 = 0

        for i in range(len(nums)):
            if c1 == 0 and nums[i] != el2:
                el1 = nums[i]
                c1 = 1
            elif c2 == 0 and nums[i] != el1:
                el2 = nums[i]
                c2 = 1
            elif nums[i] == el1:
                c1 += 1
            elif nums[i] == el2:
                c2 += 1
            else:
                c1 -= 1
                c2 -= 1
        
        minCount = len(nums)//3
        cn1 = 0
        cn2 = 0
        res = []
        for x in nums:
            if x == el1:
                cn1 += 1
            elif x == el2:
                cn2 += 1
        if cn1 > minCount:
            res.append(el1)
        if cn2 > minCount:
            res.append(el2)
        return res
        
