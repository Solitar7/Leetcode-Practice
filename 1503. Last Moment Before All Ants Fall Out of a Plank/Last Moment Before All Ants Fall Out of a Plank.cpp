class Solution {
public:
    int getLastMoment(int n, vector<int>& left, vector<int>& right) {
        int maxL = -1;
        int minR = -1;
        if (right.size() != 0){
            minR = right[0];
            for (int i = 0; i < right.size(); i++){
                if (minR > right[i]){
                    minR = right[i];
                }
            }
        }
        if (left.size() != 0){
            maxL = left[0];
            for (int i = 0; i < left.size(); i++){
                if (maxL < left[i]){
                    maxL = left[i];
                }
            }
        }
        if (minR == -1){
            return maxL;
        }
        int result = n - minR;
        if (result < maxL){
            result = maxL;
        }
        return result;
    }
};
