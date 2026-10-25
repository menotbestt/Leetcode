class Solution:
    def numEnclaves(self, grid: list[list[int]]) -> int:
        R = len(grid);C=len(grid[0])
        q = deque()
        cnt = 0
        for row in range(R):
            for col in range(C):
                if grid[row][col]:
                    if row == 0 or col == 0 or row == R-1 or col == C-1:
                        touch = True
                    else:
                        touch = False

                    grid[row][col] = 0
                    q.append((row,col))
                    temp = 1
                    while q:
                        r,c = q.popleft()
                        for x,y in (0,1),(0,-1),(1,0),(-1,0):
                            nr,nc = r+x,c+y
                            if nr < 0 or nc < 0 or nr >= R or nc>= C or not grid[nr][nc]:
                                continue
                            if not nr or not nc or nr == R-1 or nc == C-1:
                                touch = True
                            grid[nr][nc] = 0
                            q.append((nr,nc))
                            temp += 1
                    if not touch:
                        cnt += temp
        return cnt
