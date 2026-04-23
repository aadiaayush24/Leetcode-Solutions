class Solution {
    public int[] twoSum(int[] nums, int target) {
        Map<Integer, Integer> needed= new HashMap<>();
        for (int i=0; i<nums.length; i++) {
            if (needed.containsKey(target-nums[i])) {
                return new int[]{i, needed.get(target-nums[i])};
            }
            needed.put(nums[i], i);
        }
        return new int[2];
    }
}