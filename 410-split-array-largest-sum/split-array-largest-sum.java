class Solution {
    public boolean isSumPossibleInLTEKSub(int[] nums, int sum, int k) {
        int count=1;
        int currSum=0;
        for (int i: nums) {
            if (i>sum) return false;
            else if (currSum+i <= sum) {
                currSum += i;
            }
            else {
                currSum=i;
                count++;
                if (count>k) return false;
            }
        }
        return true;
    }
    public int splitArray(int[] nums, int k) {
        // int left= Arrays.stream(nums).max().getAsInt();
        // int right=Arrays.stream(nums).sum();
        int left=0, right=0;
        for (int n: nums) {
            left = Math.max(left, n);
            right += n;
        }
        
        while (left<right) {
            int mid = (left + (right-left)/2);
            if (isSumPossibleInLTEKSub(nums, mid, k)) {
                right=mid;
            }
            else {
                left=mid+1;
            }
        }
        return left;
    }
}