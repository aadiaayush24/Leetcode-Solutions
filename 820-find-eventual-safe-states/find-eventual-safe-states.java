class Solution {
    public List<Integer> eventualSafeNodes(int[][] graph) {
        Set<Integer> safeNodes = new HashSet<>();
        for (int i = 0; i < graph.length; i++) {
            if (graph[i].length == 0) {
                safeNodes.add(i);
            }
        }
        while (true) {
            int prevSize = safeNodes.size();
            for (int i = 0; i < graph.length; i++) {
                if (safeNodes.contains(i))
                    continue;
                if (Arrays.stream(graph[i]).allMatch(safeNodes::contains))
                    safeNodes.add(i);
            }
            int currSize = safeNodes.size();
            if (currSize == prevSize) {
                break;
            }
        }
        return safeNodes.stream().sorted().toList();
    }
}