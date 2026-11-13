class Solution:
    def countServers(self, grid: list[list[int]]) -> int:
        def helper(r,c):
            temp = 0
            for i in range(len(grid[0])):
                if grid[r][i] and i != c:
                    return False

            for j in range(len(grid)):
                if grid[j][c] and j != r:
                    return False                
            return True

        total = sum(j for i in grid for j in i)

        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j]:
                    if helper(i,j):
                        total -= 1
        return total