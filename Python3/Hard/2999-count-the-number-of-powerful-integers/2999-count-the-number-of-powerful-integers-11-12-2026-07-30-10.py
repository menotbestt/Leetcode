class Solution:
    def numberOfPowerfulInt(self, start: int, finish: int, l: int, s: str) -> int:
        k = len(s)
        v = int(s)
        
        # 2. 计算前缀 P 的合法范围
        # (start - v) / 10^k <= P <= (finish - v) / 10^k
        maxp = (finish - v) // (10 ** k)
        if maxp < 0:
            return 0
            
        minp = (start - v + 10 ** k - 1) // (10 ** k) # 向上取整
        minp = max(0, minp) # P 不能是负数
        
        if minp > maxp:
            return 0

        def solve(n):
            if n < 0:
                return 0
            d = list(map(int,str(n)))
            L = len(d)
            @cache
            def dfs(pos,started,tight):
                if pos == L:
                    return 1
                
                res = 0
                limit = min(l,d[pos]) if tight else l
                for cur in range(1+limit):

                    nt = tight and (d[pos] == cur)
                    ns = started or cur != 0
                    res += dfs(pos+1, ns,nt)

                return res
            return dfs(0,False,True)
        return solve(maxp) - solve(minp-1)