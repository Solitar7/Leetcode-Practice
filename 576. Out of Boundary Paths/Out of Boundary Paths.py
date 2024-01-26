class Solution:
    def findPaths(self, m: int, n: int, maxMove: int, startRow: int, startColumn: int) -> int:
        if m == 1 and n == 1:
            return 4
        grid = []
        for i in range(m+2):
            grid.append([])
            for j in range(n+2):
                grid[i].append(0)
        grid[startRow+1][startColumn+1] = 1
        result = 0
        for k in range(maxMove+1):
            print(grid)
            for i in range(m+2):
                result = result + grid[i][0] + grid[i][-1]
                grid[i][0] = 0
                grid[i][-1] = 0
            for j in range(n+2):
                result = result + grid[0][j] + grid[-1][j]
                grid[0][j] = 0
                grid[-1][j] = 0
            newG = []
            for i in range(m+2):
                newG.append([])
                if i == 0:
                    for j in range(n+2):
                        if j == 0:
                            newG[i].append(grid[i+1][j] + grid[i][j+1])
                        elif j == n+1:
                            newG[i].append(grid[i+1][j] + grid[i][j-1])
                        else:
                            newG[i].append(grid[i+1][j] + grid[i][j+1] + grid[i][j-1])
                elif i == m+1:
                    for j in range(n+2):
                        if j == 0:
                            newG[i].append(grid[i-1][j] + grid[i][j+1])
                        elif j == n+1:
                            newG[i].append(grid[i-1][j] + grid[i][j-1])
                        else:
                            newG[i].append(grid[i-1][j] + grid[i][j+1] + grid[i][j-1])
                else:
                    for j in range(n+2):
                        if j == 0:
                            newG[i].append(grid[i-1][j] + grid[i][j+1] + grid[i+1][j])
                        elif j == n+1:
                            newG[i].append(grid[i-1][j] + grid[i][j-1] + grid[i+1][j])
                        else:
                            newG[i].append(grid[i-1][j] + grid[i][j+1] + grid[i][j-1] + grid[i+1][j])
            grid = newG
        return result % (10**9 + 7)
