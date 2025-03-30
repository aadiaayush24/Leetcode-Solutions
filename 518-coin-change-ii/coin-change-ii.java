class Solution {
    public int coinDenom(int target, int index, int[][] dp, int[] coins)    {
        if (index == 0) {
            if (target%coins[index] == 0)   {
                return 1;
            }
            else {
                return 0;
            }
        }
        if (dp[index][target] != -1)    {
            return dp[index][target];
        }
        int notTaken = coinDenom(target, index-1, dp, coins);
        int taken = 0;
        if (target >= coins[index] )
            taken = coinDenom(target-coins[index], index, dp, coins);
        dp[index][target] = notTaken + taken;
        return dp[index][target];
    }

    public int change(int amount, int[] coins) {
        int[][] dp = new int[coins.length][amount+1];
        for(int[] row: dp)  {
            Arrays.fill(row, -1);
        }
        return coinDenom(amount, coins.length-1, dp, coins);
    }
}