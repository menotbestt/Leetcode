class Solution:
    def getRow(self, n: int) -> list[int]:
        
        dp = [[1]*(1+n) for i in range(1+n)]
        for i in range(1,n):
            for j in range(1,i+1):
                dp[i][j] = dp[i-1][j] + dp[i-1][j-1]
        return dp[n-1]