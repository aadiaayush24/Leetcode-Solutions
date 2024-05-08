class Solution {
public:
    vector<string> findRelativeRanks(vector<int>& score) {
        vector<int> sortedScore = score;
        sort(sortedScore.begin(), sortedScore.end(), [](int a, int b) {return a > b;});
        unordered_map<int, int> indices;
        for (int i = 0; i < sortedScore.size(); i++)  {
            indices.insert({sortedScore[i], i+1});
        } 
        vector<string> answer;
        int i = 0;
        for (int element : score)   {
            int val = indices[element];

            if (val == 1)   {
                answer.push_back("Gold Medal");
            }
            else if (val == 2)   {
                answer.push_back("Silver Medal");
            }
            else if (val == 3)   {
                answer.push_back("Bronze Medal");
            }
            else {
                answer.push_back(to_string(val));
            }
        }
        return answer;
    }
};