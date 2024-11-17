#include <stdio.h>
using namespace std;
class Solution {
public:
    int maxScore(vector<int>& cardPoints, int k) {
        int left = 0, right = cardPoints.size()-1, maxSum = 0;
        for (left = 0; left <k; left++)   {
            maxSum += cardPoints[left];
        }
        int currSum = maxSum;
        for (int i = 0; i<k; i++)   {
            currSum += cardPoints[right--] - cardPoints[--left];
            if (maxSum < currSum)   
            maxSum = currSum; 
        }
        return maxSum;
    }
};