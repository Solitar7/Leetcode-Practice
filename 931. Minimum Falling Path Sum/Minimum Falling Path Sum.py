class Solution:
    def minFallingPathSum(self, matrix: List[List[int]]) -> int:
        n = len(matrix)
        if n == 1:
            return matrix[0][0]
        curr = matrix[0][:]
        new = [0] * n
        for i in range(1,n):
            new[0] = matrix[i][0] + min(curr[0],curr[1])
            new[n-1] = matrix[i][n-1] + min(curr[n-2],curr[n-1])
            for j in range(1,n-1):
                new[j] = matrix[i][j] + min(curr[j-1],curr[j],curr[j+1])
            curr,new = new,curr
        return min(curr)
