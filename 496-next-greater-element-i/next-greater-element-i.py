class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        i = 0
        j = 0
        res = []
        while (i < len(nums1)):
            curr = nums1[i]
            j = 0
            while (nums2[j] != curr):
                j += 1
            while (j < len(nums2) and nums2[j] <= curr):
                j += 1 
            if j == len(nums2):
                res.append(-1)
            else:
                res.append(nums2[j])
            i += 1
        return res
            
