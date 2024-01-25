class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        temp = [0]*(len(text2)+1)
        dp = []
        for _ in range(len(text1)+1):
            dp.append(temp[:])
        for i in range(len(text1)):
            for j in range(len(text2)):
                if text1[i] == text2[j]:
                    dp[i+1][j+1] = max(dp[i][j]+1,dp[i][j+1],dp[i+1][j])
                else:
                    dp[i+1][j+1] = max(dp[i][j+1],dp[i+1][j])
        print(dp)
        return dp[len(text1)][len(text2)]
