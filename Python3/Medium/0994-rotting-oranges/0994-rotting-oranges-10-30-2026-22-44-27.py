class Solution:
    def orangesRotting(self, grid: list[list[int]]) -> int:
        R = len(grid)
        C = len(grid[0])
        org = False
        q = deque()
        for i in range(R):
            for j in range(C):
                if grid[i][j] == 2:
                    q.append((i,j,0))
                elif grid[i][j]:
                    org = True
        if not q and org:
            return -1

        time = 0
        while q:
            r,c,t = q.popleft()
            for x,y in (0,1),(0,-1),(1,0),(-1,0):
                nr,nc = r+x,y+c
                if nr <0 or nc<0 or nr>=R or nc>=C or grid[nr][nc] != 1:
                    continue
                q.append((nr,nc,t+1))
                grid[nr][nc] = 2
                time = max(time,t+1)
        for i in grid:
            for j in i:
                if j == 1:
                    return -1
        return time
        
