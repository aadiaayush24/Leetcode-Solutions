class Solution {
    public class Triplet {
        int row;
        int col;
        int depth;
        public Triplet(int r, int c, int d) {
            row = r;
            col = c;
            depth = d;
        }
    }
    public int shortestPathBinaryMatrix(int[][] grid) {
        if (grid[0][0] != 0) {
            return -1;
        }
        int n =grid.length;
        Deque<Triplet> dq= new ArrayDeque<Triplet>();
        int[][] visited = new int[n][n];
        Arrays.stream(visited).forEach(row -> Arrays.fill(row, -1));
        dq.add(new Triplet(0, 0, 1));
        while (!dq.isEmpty()) {
            Triplet t = dq.pollFirst();
            if (t.row == n-1 && t.col == n-1) {
                return t.depth;
            }
            int[] dr = {-1, -1, -1, 0, 0, 1, 1, 1};
            int[] dc = {-1, 0, 1, -1, 1, -1, 0, 1};
            for (int i=0 ; i<8; i++) {
                int nr = t.row+dr[i];
                int nc = t.col+dc[i];

                if (nr >= 0 && nr < n && nc >= 0 && nc < n && grid[nr][nc]!=1 &&
                visited[nr][nc] != 1) {
                    visited[nr][nc]=1;
                    dq.add(new Triplet(nr, nc, t.depth+1));
                }
            }
        }
        return -1;
    }
}