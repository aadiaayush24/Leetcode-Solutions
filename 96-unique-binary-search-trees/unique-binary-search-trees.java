class Solution {
    public int findNumTrees(int[] memo, int i) {
        if (memo[i] != -1) {
            return memo[i];
        }
        else {
            int res=0;
            for (int j=1; j<=i; j++) {
                res += findNumTrees(memo, j-1)*findNumTrees(memo, i-j);
            }
            memo[i]=res;
            return res;
        }
    }
    public int numTrees(int n) {
        // G(n) = sigma(n, i=1){G(i-1)*G(n-i)}
        int[] memo = new int[n+1];
        if (n==0 || n==1) {
            return 1;
        }

        Arrays.fill(memo, -1);
        memo[0]=1;
        memo[1]=1;
        return findNumTrees(memo, n);
    }
}