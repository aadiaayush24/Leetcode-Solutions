#include <unordered_map>
using namespace std;
class Solution {
public:
    vector<int> findAnagrams(string s, string p) {
        unordered_map<char, int> cptrn;
        for(char c: p)  {
            cptrn[c]++;
        }
        unordered_map<char, int> sptrn;
        int lPtr = 0;
        int rPtr = 0;
        vector<int> res;
        while (rPtr < s.size()) {
            char cl = s.at(rPtr); 
            if (cptrn.find(cl) != cptrn.end()) {
                if (sptrn[cl] >= cptrn[cl]) {
                    sptrn[s[lPtr]]--;
                    lPtr++;
                }
                else {
                    sptrn[cl]++;
                    rPtr++;
                }
                if (cptrn == sptrn) {
                        cout << "Found";
                        res.push_back(lPtr);
                    }
            }
            else {
                rPtr++;
                lPtr = rPtr;
                sptrn.clear();
            }
        }
        return res;
    }
};