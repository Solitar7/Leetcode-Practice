class Solution {
public:
    vector<vector<int>> onesMinusZeros(vector<vector<int>>& grid) {
        int m = grid.size();
        int n = grid[0].size();
        vector<int> onesRow(m);
        vector<int> onesColumn(n);
        for (int i = 0; i < m; i++){
            for (int j = 0; j < n; j++){
                onesRow[i] += grid[i][j];
                onesColumn[j] += grid[i][j];
            }
        }

        vector<vector<int>> result(m, vector<int>(n));
        for (int i = 0; i < m; i++){
            for (int j = 0; j < n; j++){
                result[i][j] = 2*(onesRow[i] + onesColumn[j]) - m - n;
            }
        }
        return result;
    }
};
