class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        if not nums:
            return 0
        left = 0
        right = len(nums)-1

        while (right >=0 and nums[right] == val):
            right -= 1
        
        while (left<len(nums) and right>=0 and left < right):
            if (nums[left] == val):
                nums[left], nums[right] = nums[right], nums[left]
            left += 1

            while (right>=0 and nums[right] == val):
                right -= 1

        if nums[left] != val:
            return left+1
        else:
            return left