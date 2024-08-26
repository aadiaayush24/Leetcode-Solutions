class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        i = 0
        j = 0
        l = len(nums)
        while j < l:
            while j < l and nums[i] == nums[j]:
                j += 1
            if j < l:
                i += 1
                nums[i] = nums[j]
        return i+1