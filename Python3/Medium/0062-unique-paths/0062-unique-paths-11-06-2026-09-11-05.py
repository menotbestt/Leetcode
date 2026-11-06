class Solution:
    def uniquePaths(self, R: int, C: int) -> int:
        dp = [[0]*C for i in range(R)]
        dp[0][0] = 1
        for i in range(R):
            for j in range(C):
                if i > 0:
                    dp[i][j] += dp[i-1][j]
                if j > 0:
                    dp[i][j] += dp[i][j-1]
        return dp[-1][-1]