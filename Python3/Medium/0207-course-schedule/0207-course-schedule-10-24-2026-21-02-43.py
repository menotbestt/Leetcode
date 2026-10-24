class Solution:
    def canFinish(self, c: int, p: list[list[int]]) -> bool:
        d = {}
        for a,b in p:
            if b in d:
                d[b].append(a)
            else:
                d[b] = [a]
        
        col = [0]*c #颜色标注法
        def dfs(u):
            col[u] = 1

            for v in d.get(u,[]):
                if col[v] == 1:
                    return True
                if col[v] == 0:
                    if dfs(v):
                        return True
                
            col[u] = 2
            return False
        for i in range(c):
            if not col[i] and dfs(i):
                return False
        return True
