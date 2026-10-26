class Solution:
    def countIslands(self, grid: List[List[int]], k: int) -> int:
        cnt = 0
        R=len(grid);C=len(grid[0])
        def dfs(r,c):
            nonlocal temp
            if r<0 or c<0 or r >= R or c >= C or not grid[r][c]:
                return
            temp += grid[r][c]
            grid[r][c] = 0
            dfs(r+1,c)
            dfs(r,c+1)
            dfs(r-1,c)
            dfs(r,c-1)
            
        for r in range(R):
            for c in range(C):
                if grid[r][c]:
                    temp = 0
                    dfs(r,c)
                    cnt += 0 if temp%k else 1

        return cnt
