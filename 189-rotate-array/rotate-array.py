class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        st = []
        n = len(nums)
        k = k%n
        for i in range(n-1, n-k-1, -1):
            st.append(nums[i])
        for j in range(n-1, k-1, -1):
            nums[j] = nums[j-k]
        for m in range(k):
            nums[m] = st.pop()
        return