class Solution:
    def maxScore(self, s: str) -> int:
        result = 0
        left = 0
        right = 0
        for i in s:
            if i == "1":
                right = right + 1
        for i in range(len(s)-1):
            if s[i] == "0":
                left = left + 1
            else:
                right = right - 1
            result = max(result, left + right)
        return result
