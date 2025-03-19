class Solution:
    def numberOfSubarrays(self, nums: List[int], k: int) -> int:
        nums[:] = [0 if num%2 == 0 else 1 for num in nums]
        currSum = 0
        freqTarget = {0: 1}
        count = 0
        for i in range(len(nums)):
            currSum += nums[i]
            target = currSum - k
            if target in freqTarget:
                count += freqTarget[target]
            if currSum in freqTarget:
                freqTarget[currSum] += 1
            else:
                freqTarget[currSum] = 1
        return count

                