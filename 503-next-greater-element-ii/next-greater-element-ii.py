from collections import deque
class Solution:
    def nextGreaterElements(self, nums: List[int]) -> List[int]:
        res = []
        n = len(nums)
        i = 2*n-1
        st = deque()
        while (i >= 0):
            while (st and st[-1] <= nums[i%n]):
                st.pop()
            if i < n:
                res.append(st[-1] if st else -1)
            st.append(nums[i%n])
            i -= 1
        return res[::-1]
        