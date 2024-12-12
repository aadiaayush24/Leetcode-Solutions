class Solution:
    def isBipartite(self, graph: List[List[int]]) -> bool:
        def doDfs(i, color):
            for node in graph[i]:
                if (vis[node] == -1):
                    vis[node] = not color
                    if (not doDfs(node, not color)):
                        return False
                elif vis[node] == color:
                    return False
            return True
        n = len(graph)
        vis = [-1 for i in range(n)]
        
        for i in range(n):
            if vis[i] == -1:
                if (not doDfs(i, 0)):
                    return False
        return True

                    
            