class Solution:
    def floodFill(self, grid: list[list[int]], sr: int, sc: int, color: int) -> list[list[int]]:
        cc = grid[sr][sc]
        if cc == color:
            return grid

        def dfs(r,c):
            if r<0 or r >=len(grid) or c < 0 or c >=len(grid[0]) or grid[r][c] != cc:
                return
            
            grid[r][c] = color

            dfs(r+1,c)
            dfs(r-1,c)
            dfs(r,c+1)
            dfs(r,c-1)

        dfs(sr,sc)
        return grid
