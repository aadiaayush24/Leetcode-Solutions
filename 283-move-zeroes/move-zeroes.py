class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        zi, nzi = 0, 0
        l = len(nums)
        while nzi < l:
            while (zi < l and nums[zi] != 0):
                zi += 1
            while (nzi < l and nums[nzi] == 0):
                nzi += 1
            if nzi > zi and nzi < l:
                nums[nzi], nums[zi] = nums[zi], nums[nzi]
            nzi += 1
        