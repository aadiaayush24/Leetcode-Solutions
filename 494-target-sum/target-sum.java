class Solution {
    public int cntExp(int index, int crntTarget, Map<String, Integer> dp, int[] nums)  {
        if (index == -1)    {
            return crntTarget == 0 ? 1: 0;
        }
        String key = index+","+crntTarget;
        if (dp.containsKey(key)) {
            return dp.get(key);
        }
        int addCurr = cntExp(index-1, crntTarget + nums[index], dp, nums);
        int subCurr = cntExp(index-1, crntTarget - nums[index], dp, nums);
        dp.put(key, addCurr + subCurr);
        return dp.get(key);
    }
    public int findTargetSumWays(int[] nums, int target) {
        Map<String, Integer> dp = new HashMap<>();
        return cntExp(nums.length-1, target, dp, nums);
    }
}