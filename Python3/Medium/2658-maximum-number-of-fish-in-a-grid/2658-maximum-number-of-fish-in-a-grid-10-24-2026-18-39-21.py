class Solution:
    def findMaxFish(self, grid: List[List[int]]) -> int:
        m = 0
        v = set()
        C = len(grid[0])
        R = len(grid)
        DR = (0,1),(0,-1),(-1,0),(1,0)
        for row in range(len(grid)):
            for col in range(len(grid[0])):
                if (row,col) in v or not grid[row][col]:
                    continue
                q = deque([(row,col)])
                temp = grid[row][col]
                v.add((row,col))
                while q:
                    r,c = q.popleft()
                    for x,y in DR:
                        nr,nc = x+r,c+y
                        if nr<0 or nc<0 or nr>=R or nc>=C or (nr,nc) in v or not grid[nr][nc]:
                            continue
                        temp += grid[nr][nc]
                        v.add((nr,nc))
                        q.append((nr,nc))
                m = max(m,temp)
                temp = 0
                
        return m