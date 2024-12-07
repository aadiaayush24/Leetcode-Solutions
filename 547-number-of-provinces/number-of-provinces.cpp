#include <vector>
#include <stack>
using namespace std;
class Solution {
public:
    int findCircleNum(vector<vector<int>>& isConnected) {
        int SIZE = isConnected.size();
        vector<bool> visited(SIZE, false);
        int count = 0;
        for (int ind = 0; ind < SIZE; ind++)    {
            if (visited[ind] == false)  {
                count++;
                doDFS(isConnected, visited, ind);
            }
        }
        return count;
    }

    void doDFS(vector<vector<int>>& adj, vector<bool>& visited, int v)   {
        visited[v] = true;
        for (int i = 0; i < adj[v].size(); i++)   {
            if ((i != v) && (adj[v][i] == 1) && (visited[i] == false)) {
                doDFS(adj, visited, i);
            }
        }
        return;
    }
};