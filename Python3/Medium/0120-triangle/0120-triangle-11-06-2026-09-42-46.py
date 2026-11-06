class Solution:
    def minimumTotal(self, grid: list[list[int]]) -> int:
        for row in range(len(grid)-2,-1,-1):
            for col in range(len(grid[row])):
                grid[row][col] += min(grid[row+1][col],grid[row+1][col+1])
        print(grid)
        return grid[0][0]