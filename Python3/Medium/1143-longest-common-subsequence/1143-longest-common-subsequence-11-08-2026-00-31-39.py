class Solution:
    def longestCommonSubsequence(self, t1: str, t2: str) -> int:
        m, n = len(t1), len(t2)
        dp = [0]*(1+n)

        for i in range(1, m + 1):
            prev = 0
            for j in range(1,n+1):
                temp = dp[j]
                if t1[i-1] == t2[j-1]:
                    dp[j] = prev + 1
                else:
                    dp[j] = max(dp[j-1],dp[j])
                prev = temp

        return dp[-1]