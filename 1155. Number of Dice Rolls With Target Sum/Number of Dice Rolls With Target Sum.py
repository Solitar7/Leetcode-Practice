class Solution:
    def numRollsToTarget(self, n: int, k: int, target: int) -> int:
        if n * k < target:
            return 0
        if target < n:
            return 0
        last = [0] * (target + 1)
        cur = [0] * (target + 1)
        last[0] = 1

        for i in range(1, n+1):
            for j in range(i, min(i*k, target) + 1):
                for d in range(1, min(k,j) + 1):
                    cur[j] = (cur[j] + last[j-d]) % (10**9 + 7)
            last = cur
            cur = [0] * (target + 1)
        
        return last[target]
