class Solution:
    def combinationSum3(self, k: int, n: int) -> list[list[int]]:
        res=[]
        path = []
        cur = 0
        def dfs(idx):
            nonlocal cur
            if cur == n and len(path)==k:
                res.append(path[:])
                return

            for i in range(idx,10):
                if cur + i > n:
                    break
                cur += i
                path.append(i)
                dfs(i+1)
                cur -= i
                path.pop()
        dfs(1)
        return res