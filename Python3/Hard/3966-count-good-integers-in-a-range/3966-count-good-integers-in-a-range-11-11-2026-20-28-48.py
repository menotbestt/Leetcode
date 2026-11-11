class Solution:
    def goodIntegers(self, l: int, r: int, k: int) -> int:
        def solve(n):
            digits = list(map(int,str(n)))
            L = len(digits)
            @cache
            def dfs(pos, tight, prev, good, started):
                if not good:
                    return 0
                if pos == L:
                    return 1 if good else 0
                
                res = 0
                limit = digits[pos] if tight else 9
                for cur in range(1+limit):
                    ns = started or cur != 0
                    nt = tight and digits[pos] == cur
                    newgood = abs(prev - cur) <= k or not started
                    newprev = cur if ns else 20
                    res += dfs(pos+1, nt, newprev, newgood, ns)
                return res

            return dfs(0,True,20,True,False)

        return solve(r) - solve(l-1)