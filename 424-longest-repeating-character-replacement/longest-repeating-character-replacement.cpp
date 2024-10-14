#include <unordered_map>
#include <algorithm>
using namespace std;
class Solution {
public:
    int characterReplacement(string s, int k) {
        int lPtr = 0, rPtr = 0;
        unordered_map<char, int> count;
        int maxCount = 0, maxLen = 0;
        while (rPtr < s.size()) {
            char c = s[rPtr];
            count[c]++;
            if (count[c] > maxCount)    {
                maxCount = count[c];
            }
            int lenReplace = (rPtr-lPtr+1) - maxCount;
            if (lenReplace>k) {
                count[s[lPtr]]--;
                lPtr++;
            }
            else {
                maxLen = max(maxLen, rPtr-lPtr+1);
            }
            rPtr++;
        }
    return maxLen;
    }
};