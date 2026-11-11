class Solution:
    def countSteppingNumbers(self, low: str, high: str) -> int:
        MOD = 10**9+7
        def solve(n):
            d = list(map(int,str(n)))
            L = len(d)
            @cache
            def dfs(pos,tight,start,prev,ranges):
                if not ranges:
                    return 0
                if pos == L:
                    return 1 if start and ranges else 0
                
                res = 0
                limit = d[pos] if tight else 9
                for cur in range(1+limit):
                    nt = tight and d[pos] == cur
                    ns = start or cur != 0
                    newcur = cur if ns else -2
                    newrange = not start or abs(prev-cur) == 1
                    res += dfs(pos+1,nt,ns,newcur,newrange)
                    res %= MOD
                return res
            return dfs(0,True,False,-2,True)
        return (solve(high) - solve(int(low)-1))%MOD
