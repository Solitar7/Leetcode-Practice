class Solution {
public:
    vector<int> getSumAbsoluteDifferences(vector<int>& nums) {
        int n = nums.size();
        int absSum = 0;
        std::vector<int> result(n,0);
        for(int i = 0; i < nums.size(); i++){
            absSum = absSum + nums[i];
        }
        for(int i = 0; i < nums.size(); i++){
            result[i] = absSum + i * nums[i] - (n-i) * nums[i];
            absSum = absSum - 2 * nums[i];
        }
        return result;
    }
};
