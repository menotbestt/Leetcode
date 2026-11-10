class Solution:
    def climbStairs(self, n: int, costs: List[int]) -> int:
        dp = [inf]*(n+1)
        dp[0] = 0
        for i in range(1,n+1):
            for j in [1,2,3]:
                if i - j >= 0:
                    dp[i] = min(dp[i-j] + costs[i-1] + j**2, dp[i])
        return dp[-1]