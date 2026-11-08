class Solution:
    def longestPalindromeSubseq(self, s: str) -> int:
        n = len(s)
        dp = [0]*(1+n)
        for i in range(n,0,-1):
            prev = 0
            for j in range(1,n+1):
                temp = dp[j]
                if s[j-1] == s[i-1]:
                    dp[j] = prev + 1
                else:
                    dp[j] = max(dp[j-1],dp[j])
                prev = temp

        return dp[-1]