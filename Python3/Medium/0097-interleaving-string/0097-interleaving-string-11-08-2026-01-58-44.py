class Solution:
    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:
        n = len(s1)
        m = len(s2)
        if n+m!=len(s3):
            return False
        dp = [[False]*(m+1) for i in range(n+1)]
        dp[0][0] = True
        for i in range(1,1+n):
            dp[i][0] = dp[i-1][0] and s1[i-1] == s3[i-1]
        for i in range(1,1+m):
            dp[0][i] = dp[0][i-1] and s2[i-1] == s3[i-1]
        
        for i in range(1,n+1):
            for j in range(1,m+1):
                dp[i][j] = dp[i-1][j] and s1[i-1] == s3[i+j-1]\
                                      or                      \
                           dp[i][j-1] and s2[j-1] == s3[i+j-1]
        return dp[-1][-1]
