class Solution:
    def longestPalindromeSubseq(self, s: str) -> int:
        n = len(s)
        rev = s[::-1]
        dp = [0]*(1+n)
        for i in range(1,n+1):
            prev = 0
            for j in range(1,n+1):
                temp = dp[j]
                if rev[j-1] == s[i-1]:
                    dp[j] = prev + 1
                else:
                    dp[j] = max(dp[j-1],dp[j])
                prev = temp

        return dp[-1]