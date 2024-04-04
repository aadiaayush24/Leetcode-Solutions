class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        numDict = {}
        for i in range(len(nums)):
            n = nums[i]
            if n in numDict and i - numDict[n] <=k:
                return True
            else:
                numDict[n] = i 
        return False