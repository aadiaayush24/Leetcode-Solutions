class Solution {
    public void rotate(int[][] matrix) {
        // Interchange row order (last row becomes first, second last becomes second etc)
        int n = matrix.length;
        for (int i=0; i<n/2; i++) {
            int[] temp = new int[n];
            temp=matrix[i];
            matrix[i]=matrix[n-1-i];
            matrix[n-1-i]=temp;
        }
        // 
        int t;
        for (int i=0; i<n; i++) {
            for (int j=i+1; j<n; j++) {
                t = matrix[i][j];
                matrix[i][j]=matrix[j][i];
                matrix[j][i] = t;
            }
        }
    }

}