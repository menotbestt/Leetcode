class Solution:
    def combine(self, n: int, k: int) -> list[list[int]]:
        res = []
        path = []
        v = set()
        def dfs(start):
            if len(path) == k:
                res.append(path[:])
                return
            
            for i in range(start+1,n+1):
                path.append(i)
                dfs(i)
                path.pop()
        dfs(0)
        return res
