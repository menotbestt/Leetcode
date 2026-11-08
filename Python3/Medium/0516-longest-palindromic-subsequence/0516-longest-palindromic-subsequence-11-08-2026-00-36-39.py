class Solution:
    def longestPalindromeSubseq(self, s: str) -> int:
        n = len(s)
        rev = s[::-1]
        dp = [[0]*(1+n) for _ in range(n+1)]
        for i in range(1,n+1):
            for j in range(1,n+1):
                if rev[j-1] == s[i-1]:
                    dp[i][j] = dp[i-1][j-1] + 1
                else:
                    dp[i][j] = max(dp[i-1][j],dp[i][j-1])

        return dp[-1][-1]