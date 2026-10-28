class Solution:
    def minCost(self, grid: list[list[int]]) -> int:
        dp = [set()] * len(grid[0])
        dp[0] = set([0])
        
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                prev = dp[j].union(dp[j - 1]) if j else dp[j]
                dp[j] = set(x ^ grid[i][j] for x in prev)                

        return min(dp[-1])