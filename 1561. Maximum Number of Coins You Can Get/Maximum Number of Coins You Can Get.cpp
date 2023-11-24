class Solution {
public:
    int maxCoins(vector<int>& piles) {
        sort(piles.begin(),piles.end());
        int result = 0;
        int i = piles.size() / 3;
        while(i < piles.size()){
            result = result + piles[i];
            i = i + 2;
        }
        return result;
    }
};
