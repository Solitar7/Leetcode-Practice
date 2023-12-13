class Solution:
    def numSpecial(self, mat: List[List[int]]) -> int:
        row_sum = [0] * len(mat)
        column_sum = [0] * len(mat[0])
        row_ones_pos = [-1] * len(mat)
        for i in range(len(mat)):
            for j in range(len(mat[0])):
                row_sum[i] += mat[i][j]
                column_sum[j] += mat[i][j]
                if row_ones_pos[i] < 0:
                    if mat[i][j] == 1:
                        row_ones_pos[i] = j
        result = 0
        for i in range(len(row_sum)):
            if row_sum[i] == 1:
                if column_sum[row_ones_pos[i]] == 1:
                    result = result + 1
        return result
