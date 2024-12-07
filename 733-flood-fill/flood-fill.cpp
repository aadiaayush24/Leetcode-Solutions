#include <queue>
#include <vector>
using namespace std;
class Solution {
public:
    vector<vector<int>> floodFill(vector<vector<int>>& image, int sr, int sc, int color) {
        int orig_color = image[sr][sc];
        queue<pair<int, int>> pixels;
        pixels.push({sr, sc});
        int m = image.size();
        int n = image[0].size();
        if (orig_color == color)    {
            return image;
        }
        while (!pixels.empty()) {
            pair<int, int> currPixel = pixels.front();
            int x = currPixel.first, y = currPixel.second;
            image[x][y] = color;
            vector<pair<int, int>> dirs = {{-1,0}, {1,0}, {0,1}, {0,-1}};

            for(const auto& dir: dirs)  {
                int dx = dir.first, dy = dir.second;
                if (( x+ dx >= 0 && x+dx < m && y+dy >= 0 && y+dy < n && image[x+dx][y+dy] == orig_color))   {
                    pixels.push({x+dx, y+dy});
                }
            }
            pixels.pop();
        }
        return image;

    }
};