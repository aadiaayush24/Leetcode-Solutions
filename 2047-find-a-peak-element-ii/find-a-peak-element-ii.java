class Solution {
    public int[] findPeakGrid(int[][] mat) {
        int m = mat.length, n = mat[0].length;
        int start=0, end=n-1;
        while (start <= end) {
            int mid=(start+end)/2;
            int maxRow=0;

            for (int i=0; i<m; i++) {
                if (mat[i][mid] > mat[maxRow][mid]) {
                    maxRow = i;
                }
            }

            int leftVal = (mid-1 >=0) ? mat[maxRow][mid-1]:-1;
            int rightVal = (mid+1 < n) ? mat[maxRow][mid+1]:-1;

            if (mat[maxRow][mid] > leftVal && mat[maxRow][mid] > rightVal) {
                return new int[]{maxRow, mid};
            }
            else if (mat[maxRow][mid] < rightVal) {
                start=mid+1;
            }
            else {
                end=mid-1;
            }
        }
    
        return new int[]{-1, -1};
    }
}