#include <stack>
#include <vector>
class Solution {
public:
    vector<int> nextGreaterElements(vector<int>& nums) {
        std::stack<int> st;
        std::vector<int> res;
        int n = nums.size();
        int j = 0;
        for (int i = 2*n-1; i >=0; i--)   {
            while (!st.empty() and st.top() <= nums[i%n])
                st.pop();
            if (i < n)  {
                int r = st.empty()? -1 : st.top();
                res.push_back(r);
            }
            st.push(nums[i%n]);
        }
        res = vector<int>(res.rbegin(), res.rend());
        return res;
    }
};