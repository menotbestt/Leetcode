class Solution:
    def combinationSum2(self, c: list[int], t: int) -> list[list[int]]:
        c = sorted(c)
        res = []
        path = []
        cur= 0
        def dfs(n):
            nonlocal cur
            if cur == t:
                res.append(path[:])
                return
            
            for i in range(n+1,len(c)):
                if c[i] + cur > t:
                    break
                if i > n+1 and c[i] == c[i-1]:
                    continue
                cur += c[i]
                path.append(c[i])
                dfs(i)
                cur -= c[i]
                path.pop()
    
        dfs(-1)
        return res
