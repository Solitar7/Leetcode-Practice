class Solution {
public:
    int maximumElementAfterDecrementingAndRearranging(vector<int>& arr) {
        sort(arr.begin(),arr.end());
        int count = 1;
        for (int i = 1; i < arr.size(); i++){
            if (arr[i] > count){
                count = count + 1;
            }
        }
        return count;
    }
};
