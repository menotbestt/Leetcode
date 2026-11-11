class Solution:
    def numberOfBeautifulIntegers(self, low: int, high: int, k: int) -> int:
        def solve(n):
            d = list(map(int,str(n)))
            L = len(d)
            if L == 1:
                return 0
            @cache
            def dfs(pos,started,tight, evenodd, total):
                if abs(evenodd) > L - pos:
                    return 0
                if pos == L:
                    return 1 if started and not evenodd and not total else 0
                
                res = 0
                limit = d[pos] if tight else 9
                for cur in range(1+limit):
                    nt = tight and d[pos] == cur
                    ns = started or cur != 0
                    if not started and not cur:
                        res += dfs(pos+1,ns,nt,0,total)
                    else:
                        neweo = evenodd + (1 if cur%2 else -1)
                        newtotal = (10*total + cur) %k
                        res += dfs(pos+1,ns,nt,neweo, newtotal)
                return res

            return dfs(0,False,True,0,0)
        return solve(high) - solve(low-1)

