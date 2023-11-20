class Solution {
public:
    int garbageCollection(vector<string>& garbage, vector<int>& travel) {
        int countM = 0;
        int countP = 0;
        int countG = 0;
        int result = 0;
        int cost = 0;
        for (int i = 0; i < travel.size(); i++){
            result = result + garbage[i].length();
            cost = cost + travel[i];
            if(garbage[i+1].find("M") != string::npos){
                countM = cost;
            }
            if(garbage[i+1].find("P") != string::npos){
                countP = cost;
            }
            if(garbage[i+1].find("G") != string::npos){
                countG = cost;
            }
        }
        result = result + garbage[garbage.size()-1].length() + countM + countP + countG;
        return result;
    }
};
