class Solution:
    def mostPoints(self, q: list[list[int]]) -> int:
        n = len(q)
        dp = [0] * (n+1)
        for i in range(n-1,-1,-1):
            dp[i] = max(dp[i+1], dp[min(i + q[i][1] + 1, n)] + q[i][0])
        return dp[0]