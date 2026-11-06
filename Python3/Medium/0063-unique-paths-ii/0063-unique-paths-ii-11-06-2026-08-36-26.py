class Solution:
    def uniquePathsWithObstacles(self, grid: list[list[int]]) -> int:
        if grid[0][0] or grid[-1][-1]:
            return 0
        R = len(grid)
        C = len(grid[0])
        dp = [[0]*(C) for i in range(R)]
        dp[0][0] = 1
        for r in range(R):
            for c in range(C):
                if grid[r][c]:
                    continue
                if r > 0:
                    dp[r][c] += dp[r-1][c]
                if c > 0:
                    dp[r][c] += dp[r][c-1]

        return dp[R-1][C-1]
