#include <unordered_map>
#include <stack>
using namespace std;
class Solution {
public:
    bool isValid(string s) {
        unordered_map<char, char> bracks = {
            {')','('},
            {'}','{'},
            {']','['}
        };
        stack<char> br;

        for (const char& ch: s) {
            if (bracks.find(ch)!=bracks.end()){
                if (br.empty() || br.top() != bracks[ch])
                    return false;
                else
                    br.pop();}
            else
                br.push(ch);
        }
        if (!br.empty())
            return false;
        return true;
    }
};