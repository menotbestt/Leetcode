class Solution:
    def countIslands(self, grid: List[List[int]], k: int) -> int:
        cnt = 0
        R=len(grid);C=len(grid[0])
            
        for i in range(R):
            for j in range(C):
                if grid[i][j]:
                    stack = [(i,j)]
                    temp = 0
                    while stack:
                        r,c = stack.pop()
                        if r<0 or c< 0 or r>=R or c>=C or not grid[r][c]:
                            continue
                        temp += grid[r][c]
                        grid[r][c] = 0
                        stack += [(r+1,c),(r,c+1),(r-1,c),(r,c-1)]
                    cnt += 0 if temp%k else 1

        return cnt
