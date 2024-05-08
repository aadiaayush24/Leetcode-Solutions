class Solution {
public:
    vector<int> searchRange(vector<int>& nums, int target) {
        int last = nums.size() - 1;
        int start = 0, end =last ;
        int mid;
        vector<int> ans = {-1, -1};
        while (start <= end)    {
            int mid = start + (end - start)/2;
            if (nums[mid] == target) {
                ans[0] = mid;
                end = mid-1;
            }
            else if (nums[mid] < target)    {
                start = mid + 1;
            }
            else    {
                end = mid - 1;
            }
        }
        start = 0, end =last ;
        while (start <= end)    {
            int mid = start + (end - start)/2;
            if (nums[mid] == target) {
                ans[1] = mid;
                start = mid+1;
            }
            else if (nums[mid] < target)    {
                start = mid + 1;
            }
            else    {
                end = mid - 1;
            }
        }
        return ans;

    }
};