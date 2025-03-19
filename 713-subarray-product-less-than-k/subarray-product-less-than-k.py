class Solution:
    def numSubarrayProductLessThanK(self, nums: List[int], k: int) -> int:
        currProd = 1
        count = 0
        start = 0
        for end in range(len(nums)):
            currProd *= nums[end]
            if (nums[end] >= k):
                currProd = 1
                start = end + 1
                continue
            while (start < end and currProd >= k):
                currProd /= nums[start]
                start += 1
            count += end - start + 1
        return count
            

            
            