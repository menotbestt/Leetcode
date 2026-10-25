class Solution:
    def closedIsland(self, grid: list[list[int]]) -> int:
        R = len(grid);C=len(grid[0])
        q = deque()
        #v = set() This can simply be removed by replace visited places from 0 to 1
        cnt = 0
        for row in range(R):
            for col in range(C):
                if not grid[row][col]:
                    if row == 0 or col == 0 or row == R-1 or col == C-1:
                        touch = True
                    else:
                        touch = False

                    grid[row][col] = 1
                    q.append((row,col))

                    while q:
                        r,c = q.popleft()
                        for x,y in (0,1),(0,-1),(1,0),(-1,0):
                            nr,nc = r+x,c+y
                            if nr < 0 or nc < 0 or nr >= R or nc>= C or grid[nr][nc] == 1:
                                continue
                            if not nr or not nc or nr == R-1 or nc == C-1:
                                touch = True
                            grid[nr][nc] = 1
                            q.append((nr,nc))
                    if not touch:
                        cnt += 1
        return cnt
