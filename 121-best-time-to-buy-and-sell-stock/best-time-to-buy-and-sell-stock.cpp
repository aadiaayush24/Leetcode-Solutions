#include <vector>
#include <stack>
using namespace std;

class Solution {
public:
    int maxProfit(vector<int>& prices) {
        int maxProfit = 0;
        int buyPrice = prices[0];
        for (int i = 1; i < prices.size(); i++) {
            int price = prices[i];
            if (price < buyPrice)  {
                buyPrice = price;
            }
           else if (price > buyPrice && maxProfit < (price - buyPrice))    {
                maxProfit = price - buyPrice;
            }
            
        }
        return maxProfit;
    }
};