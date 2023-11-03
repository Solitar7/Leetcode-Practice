class Solution {
public:
    vector<string> buildArray(vector<int>& target, int n) {
        vector<string> result;
        int last = 0;
        int skip;
        for (int i = 0; i < target.size(); i++){
            skip = target[i] - last - 1;
            for (int j = 0; j < skip; j++){
                result.push_back("Push");
                result.push_back("Pop");
            }
            result.push_back("Push");
            last = target[i];
        }
        return result;
    }
};
