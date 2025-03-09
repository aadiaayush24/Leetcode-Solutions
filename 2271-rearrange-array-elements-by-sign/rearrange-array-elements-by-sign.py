class Solution:
    def rearrangeArray(self, nums: List[int]) -> List[int]:
        posInd, negInd = 0, 1
        res = [0 for _ in range(len(nums))]
        for i in range(0, len(nums)):
            if nums[i] > 0:
                res[posInd] = nums[i]
                posInd += 2
            else:
                res[negInd] = nums[i]
                negInd += 2
        return res
