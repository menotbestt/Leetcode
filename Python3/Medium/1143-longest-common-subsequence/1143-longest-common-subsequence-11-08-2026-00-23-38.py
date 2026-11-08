class Solution:
    def longestCommonSubsequence(self, t1: str, t2: str) -> int:
        m, n = len(t1), len(t2)
        dp = [[0]*(1+n) for i in range(m+1)]

        for i in range(1, m + 1):
            for j in range(1, n + 1):
                if t1[i-1] == t2[j-1]:
                    dp[i][j] = dp[i-1][j-1] + 1
                else:
                    dp[i][j] = max(dp[i-1][j],dp[i][j-1])

        return dp[m][n]