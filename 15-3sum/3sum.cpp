#include<algorithm>
using namespace std;
class Solution {
public:
    vector<vector<int>> threeSum(vector<int>& nums) {
        sort(nums.begin(), nums.end());
        int l = nums.size()-1;
        vector<vector<int>> res;
        for (int i=0; i<l-1;i++) {
            if (nums[i] > 0)    {
                break;
            }
            if (i > 0 && nums[i] == nums[i-1]) {
                continue;
            } 
            int j = i+1;
            int k = l;
            while (j < k)   {
                int currSum = nums[i] + nums[j] + nums[k];
                if (currSum == 0)   {
                    res.push_back(vector<int>{nums[i], nums[j], nums[k]});
                    while ( j<k && nums[j] == nums[j+1]) j++;
                    while ( j<k && nums[k] == nums[k-1]) k--;
                    j++;
                    k--; 
                }
                else if (currSum < 0)   {
                    j++;
                }
                else    {
                    k--;
                }
            }
        }
        return res;
    }
};