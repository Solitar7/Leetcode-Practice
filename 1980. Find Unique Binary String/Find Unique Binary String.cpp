class Solution {
public:
    string findDifferentBinaryString(vector<string>& nums) {
        string result = "";
        for (int i = 0; i < nums.size(); i++){
            if (nums[i][i] == '0'){
                result = result + "1";
            }
            else{
                result = result + "0";
            }
        }
        return result;
    }
};
