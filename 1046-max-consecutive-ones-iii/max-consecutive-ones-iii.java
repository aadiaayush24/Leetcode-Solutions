class Solution {
    public int longestOnes(int[] nums, int k) {
        int currZeroes = 0;
        int maxLength = 0;
        int left = 0;
        for (int right = 0; right< nums.length; right++)    {
            if (nums[right] == 0)   {
                while (left <= right && currZeroes == k) {
                    if (nums[left] == 0)    {
                        currZeroes--;
                    }
                    left++;
                }
                currZeroes++;
            }
            int length = right - left + 1;
            maxLength = Math.max(maxLength, length);
        }
        return maxLength;
    }
}