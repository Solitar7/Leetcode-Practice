class Solution:
    def onesMinusZeros(self, grid: List[List[int]]) -> List[List[int]]:
        m = len(grid)
        n = len(grid[0])
        ones_row = [0] * m
        ones_column = [0] * n
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                ones_row[i] += grid[i][j]
                ones_column[j] += grid[i][j]
        result = []
        for i in range(len(grid)):
            result.append([])
            for j in range(len(grid[0])):
                result[i].append(2*(ones_row[i] + ones_column[j]) - m - n)
        return result
