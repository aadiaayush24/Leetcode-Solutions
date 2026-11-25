class Solution {
    public int findCircleNum(int[][] isConnected) {
        int n = isConnected.length;
        boolean vis[] = new boolean[n];
        int pro = 0;

        for (int i=0; i<n; i++) {
            if (vis[i]) continue;
            pro++;
            Deque<Integer> dq = new ArrayDeque<Integer>();
            dq.add(i);
            vis[i] = true;
            while (!dq.isEmpty()) {
                int node = dq.poll();
                for (int j=0; j<n; j++) {
                    if (isConnected[node][j]==1 && !vis[j]) {
                        vis[j]=true;
                        dq.add(j);
                    }
                }
            }
        }
        return pro;
    }
}