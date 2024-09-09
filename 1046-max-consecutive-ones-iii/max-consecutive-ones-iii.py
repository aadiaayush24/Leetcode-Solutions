class Solution:
    def longestOnes(self, nums: List[int], k: int) -> int:
        left = 0
        right = 0
        zeroes = 0
        maxLen = 0

        while (right < len(nums)):
            if (nums[right] == 0):
                zeroes += 1
            if (zeroes > k):
                while (nums[left] != 0):
                    left += 1
                zeroes -= 1
                left += 1
            else:
                length = right - left + 1
                maxLen = max(maxLen, length)
            right += 1
        return maxLen
        