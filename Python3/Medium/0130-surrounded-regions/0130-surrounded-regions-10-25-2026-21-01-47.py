class Solution:
    def solve(self, grid: list[list[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        q =deque()
        R = len(grid)
        C = len(grid[0])

        for row in range(len(grid)):
            for col in range(len(grid[0])):
                if grid[row][col] =='O':
                    if not row or not col or row==R-1 or col==C-1:
                        q.append((row,col))
                        grid[row][col] = '.'
                        while q:
                            r,c = q.popleft()
                            for x,y in (0,1),(0,-1),(-1,0),(1,0):
                                nr,nc = x+r,c+y
                                if nr < 0 or nc < 0 or nr>=R or nc>=C or grid[nr][nc]!='O':
                                    continue
                                q.append((nr,nc))
                                grid[nr][nc] = '.'
                                
        for i in grid:
            for j in range(len(i)):
                if i[j] == 'O': i[j] ='X'
                elif i[j] =='.':i[j] = 'O'
                
