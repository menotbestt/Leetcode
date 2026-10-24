class Solution:
    def combinationSum(self, c: list[int], t: int) -> list[list[int]]:
        res = []
        path =[]
        cur = 0
        def dfs(n):
            nonlocal cur
            if cur == t:
                res.append(path[:])
                return

            for i in range(n,len(c)):
                if c[i] + cur > t:
                    continue

                path.append(c[i])
                cur += c[i]
                dfs(i)
                cur -= c[i]
                path.pop()

        dfs(0)
        return res
