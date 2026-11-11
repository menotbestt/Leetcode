class Solution:
    def countNumbers(self, l: str, r: str, b: int) -> int:
        def convert(n):
            temp = ''
            n = int(n)
            while n > 0:
                temp += str(n%b)
                n //= b
            return temp[::-1]
        MOD = 10**9 + 7
        l = int(l)-1
        r = convert(r)
        l = convert(l)
        print(l,r)
        def solve(n):
            d = list(map(int,str(n)))
            L = len(d)

            @cache
            def dfs(pos, tight, started, prev, decreased):
                if decreased:
                    return 0
                if pos == L:
                    return 0 if decreased else 1

                res = 0
                limit = d[pos]+1 if tight else b
                for cur in range(limit):
                    ns = started or cur != 0
                    nt = tight and d[pos] == cur 
                    newprev = cur if ns else -1
                    newdec = started and prev > cur 
                    res += dfs(pos+1,nt, ns, newprev, newdec)
                return res
            return dfs(0,True,False,-1,False)

        return (solve(r) - solve(l)) % MOD