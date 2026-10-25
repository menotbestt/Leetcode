class Solution:
    def solve(self, grid: list[list[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        q =deque()
        R = len(grid)
        C = len(grid[0])
        v = set()
        res = []
        for row in range(len(grid)):
            for col in range(len(grid[0])):
                if grid[row][col] =='O' and (row,col) not in v:
                    if not row or not col or row==R-1 or col==C-1:
                        touch = True
                        temp = []
                    else:
                        touch = False
                        temp = [(row,col)]
                    v.add((row,col))
                    q.append((row,col))
                    
                    while q:
                        r,c = q.popleft()
                        for x,y in (0,1),(0,-1),(-1,0),(1,0):
                            nr,nc = x+r,c+y
                            if (nr,nc) in v or nr < 0 or nc < 0 or nr>=R or nc>=C or grid[nr][nc]!='O':
                                continue
                            if not nr or not nc or nr == R-1 or nc == C-1:
                                touch = True
                            q.append((nr,nc))
                            v.add((nr,nc))
                            temp.append((nr,nc))
                    if not touch:
                        res.extend(temp)
        for x,y in res:
            grid[x][y] = 'X'
