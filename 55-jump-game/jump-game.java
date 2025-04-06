class Solution {
    public boolean nextJump(int index, int[] nums, Set<Integer> visited)    {
        if (index >= nums.length-1)    {
            return true;
        }
        if (nums[index] == 0 || visited.contains(index))    {
            return false;
        }

        int start = 1;
        int end = nums[index];
        for (int i = start; i <= end; i++)   {
            boolean canReachEnd = nextJump(index + i, nums, visited);
            if (canReachEnd)    {
                return true;
            }
        }
        visited.add(index);
        return false;
    }
    public boolean canJump(int[] nums) {
        Set<Integer> visited = new HashSet<>();
        return nextJump(0, nums, visited);
    }
}