class Solution {
    public int numberOfArithmeticSlices(int[] nums) { 
        int n = nums.length;
        int k = 3;
        if (n < k) return 0;
        int l = 0, r = 0;
        int total = 0;
        int diff = nums[1]-nums[0];
        while (r<n) {
            if (r+1<n && nums[r+1]-nums[r]==diff) {
                r++;
            }
            else {
                int len = r-l+1;
                if (len>=k) {
                    total += (len-k+1)*(len-k+2)/2;
                }
                l = r;
                if (r+1<n) {
                    diff = nums[r+1]-nums[r];
                }
                r++;
            }
        }
        return total;
}
}
