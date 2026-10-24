class Solution:
    def findMaxFish(self, grid: List[List[int]]) -> int:
        m = 0
        C = len(grid[0])
        R = len(grid)
        DR = (0,1),(0,-1),(-1,0),(1,0)

        for row in range(len(grid)):
            for col in range(len(grid[0])):
                if not grid[row][col]:
                    continue

                q = deque([(row,col)])
                temp = grid[row][col]
                grid[row][col] = 0
                while q:
                    r,c = q.popleft()
                    for x,y in DR:
                        nr,nc = x+r,c+y
                        if nr<0 or nc<0 or nr>=R or nc>=C or not grid[nr][nc]:
                            continue

                        temp += grid[nr][nc]
                        q.append((nr,nc))
                        grid[nr][nc] = 0

                m = max(m,temp)

        return m