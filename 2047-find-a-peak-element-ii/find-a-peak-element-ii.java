class Solution {
    public int[] findPeakGrid(int[][] mat) {
        int maxElem = -1;
        int[] maxInd = new int[2];
        int m = mat.length, n = mat[0].length;
        for (int i=0; i<m; i++) {
            for (int j=0; j<n; j++) {
                if (mat[i][j] > maxElem) {
                    maxElem = mat[i][j];
                    maxInd[0] = i;
                    maxInd[1] = j;
                }
                
            }
        }
        return maxInd;
    }
}