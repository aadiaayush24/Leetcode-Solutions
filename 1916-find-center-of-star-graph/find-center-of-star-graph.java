class Solution {
    public int findCenter(int[][] edges) {
        int e = edges.length;
        HashMap<Integer, Integer> degree = new HashMap<>();
        int maxDegree = 0, maxV = -1;

        for (int i=0; i<e; i++) {
            degree.put(edges[i][0], degree.getOrDefault(edges[i][0], 0)+1);
            degree.put(edges[i][1], degree.getOrDefault(edges[i][1], 0)+1);

            if (degree.get(edges[i][0])>maxDegree) {
                maxDegree=degree.get(edges[i][0]);
                maxV=edges[i][0];
            }
            else if (degree.get(edges[i][1])>maxDegree) {
                maxDegree=degree.get(edges[i][1]);
                maxV=edges[i][1];
            }
        }
        return maxV;
    }
}