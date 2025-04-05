class Solution {
    public List<List<Integer>> threeSum(int[] nums) {
        Arrays.sort(nums);
        int n = nums.length;
        int j, k;
        List<List<Integer>> res = new ArrayList<>();
        for (int i = 0; i < n-2; i++)   {
            if(nums[i] > 0) {
                break;
            }
            if (i > 0 && nums[i] == nums[i-1])  {
                continue;
            }
            j = i+1;
            k = n-1;
            while (j < k)   {
                int currSum = nums[i] + nums[j] + nums[k];
                if (currSum == 0)   {
                    res.add(new ArrayList<>(Arrays.asList(nums[i], nums[j], nums[k])));
                    while (j < k && nums[j] == nums[j+1]) j++;
                    while (j < k && nums[k] == nums[k-1]) k--;
                    j++;
                    k--;
                }
                else if (currSum > 0)   {
                    k--;
                }
                else
                    j++;
            }
        }
        return res;
    }
}