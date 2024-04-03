class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        currSum = 0
        minSize = float('inf')
        left = 0
        for right in range(len(nums)):
            currSum += nums[right]
            while currSum >= target:
                currSum -= nums[left]
                minSize = min(minSize, right-left+1)
                left += 1
        
        return 0 if minSize == float('inf') else minSize
        
             
