class Solution {
    
    public int orangesRotting(int[][] grid) {
        int m = grid.length;
        int n = grid[0].length;
        boolean[][] vis = new boolean[m][n];
        final int[] dX = {-1, 0, 0, 1};
        final int[] dY = {0, -1, 1, 0};
        Deque<int[]> deque = new ArrayDeque<>(); 

        for (int i=0; i<m; i++) {
            for (int j=0; j<n; j++) {
                if (grid[i][j] == 2) {
                    deque.add(new int[]{i, j, 0});
                    vis[i][j]=true;
                }
                else if (grid[i][j] == 1) {
                    vis[i][j]=false;
                }
                else {
                    vis[i][j]=true;
                }
            }
        }
        int d=0;
        while (!deque.isEmpty()) {
            int[] trip = deque.poll();
            d=trip[2];
            for (int i =0; i<4; i++) {
                int x_ = trip[0]+dX[i];
                int y_ = trip[1]+dY[i];

                if (x_>=0 && x_<m && y_>=0 && y_<n && !vis[x_][y_]) {
                    vis[x_][y_]=true;
                    deque.add(new int[]{x_, y_, d+1});
                }
            }
        }
        for (int i=0; i<m; i++) {
            for (int j=0; j<n; j++) {
                if (!vis[i][j]) {
                    return -1;
                }
            }
        }
        return d;

    }
}