class Solution:
    def findCircleNum(self, grid: List[List[int]]) -> int:
        n = len(grid)
        visited = [False]*n
        cnt = 0
        for i in range(n):
            if not visited[i]:
                q = deque([i])
                cnt += 1
                visited[i] = True
                while q:
                    c = q.popleft()
                    for j in range(n): # This works because each item in grid states that which index 
                                       # are connected to each other with status 0/1
                        if not visited[j] and grid[c][j]:
                            visited[j] = True
                            q.append(j)
        return cnt      