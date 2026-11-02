class Solution:
    def minPathSum(self, grid: list[list[int]]) -> int:
        R = len(grid)
        C = len(grid[0])
        dp = [[inf] * (C+1) for _ in range(R+1)]
        dp[1][0] = 0 #Force first pick to be 0 + grid[0][0] or use Prefix Sum for initilisation to avoid bug
        for r in range(1,R+1):
            for c in range(1,C+1):
                dp[r][c] = min(dp[r-1][c],dp[r][c-1]) + grid[r-1][c-1]
        return dp[-1][-1]
