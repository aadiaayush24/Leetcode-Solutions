class Solution {
    public List<Integer> findSmallestSetOfVertices(int n, List<List<Integer>> edges) {
        List<List<Integer>> reverse_adj_list = new ArrayList<>();

        // edges = [[0,1],[0,2],[2,5],[3,4],[4,2]]
        // reverse_adj_list = [[], [0], [0, 4], [], [3], [2]]

        for (int i=0; i<n; i++) {
            reverse_adj_list.add(new ArrayList<>());
        }

        for (int j=0; j<edges.size(); j++) {
            reverse_adj_list.get(edges.get(j).get(1)).add(edges.get(j).get(0));
        }

        List<Integer> startNodes = new ArrayList<>();

        for (int i=0; i<n; i++) {
            if (reverse_adj_list.get(i).size() == 0) {
                startNodes.add(i);
            }
        }
        return startNodes;
    }
}