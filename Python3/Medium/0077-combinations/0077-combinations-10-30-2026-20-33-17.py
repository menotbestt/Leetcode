class Solution:
    def combine(self, n: int, k: int) -> list[list[int]]:
        res = []
        def dfs(idx,path):
            if len(path) == k:
                res.append(path[:])
                return
            
            for i in range(idx,n+1):
                dfs(i+1,path+[i])
                
        dfs(1,[])
        return res