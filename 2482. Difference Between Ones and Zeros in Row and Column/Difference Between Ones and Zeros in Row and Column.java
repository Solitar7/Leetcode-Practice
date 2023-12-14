class Solution {
    public int[][] onesMinusZeros(int[][] grid) {
        int m = grid.length;
        int n = grid[0].length;
        int[] onesRow = new int[m];
        int[] onesColumn = new int[n];
        for (int i = 0; i < m; i++){
            for (int j = 0; j < n; j++){
                onesRow[i] += grid[i][j];
                onesColumn[j] += grid[i][j];
            }
        }

        int[][] result = new int[m][n];
        for (int i = 0; i < m; i++){
            for (int j = 0; j < n; j++){
                result[i][j] = 2*(onesRow[i] + onesColumn[j]) - m - n;
            }
        }
        return result;
    }
}
