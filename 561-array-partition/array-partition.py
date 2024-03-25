class Solution:
    def arrayPairSum(self, nums: List[int]) -> int:
        nums.sort()
        sum_ = 0
        for num in nums[::2]:
            sum_ += num
        return sum_
