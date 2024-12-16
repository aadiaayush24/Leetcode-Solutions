class Solution {
public:
    void swap(vector<int> &nums, int i, int j)  {
        int t = nums[i];
        nums[i] = nums[j];
        nums[j] = t;
        return;
    }
    void sortColors(vector<int>& nums) {
        int left = 0, mid = 0, right = nums.size()-1;

        while (mid <= right)    {
            if (nums[mid] == 0) {
                swap(nums, mid++, left++);
            }
            else if(nums[mid] == 1) {
                mid++;
            }
            else {
                swap(nums, right--, mid);
            }
        }
        return;
    }
};