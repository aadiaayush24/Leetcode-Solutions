class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        def reverse(start, end):
            if start < end:
                nums[start], nums[end] = nums[end], nums[start]
                reverse(start+1, end-1)
            return
        k = k % len(nums)
        l = len(nums)-1
        reverse(l-k+1, l)
        reverse(0, l-k)
        reverse(0, l)
        return    