class Solution:
    def findIntegers(self, n: int) -> int:
        n = bin(n)[2:]
        digits = list(map(int,n))
        L = len(digits)
        @cache
        def dfs(pos,tight,prev,repeated):
            if pos == L:
                return 0 if repeated else 1
            
            res = 0
            limit = digits[pos] if tight else 1
            for cur in range(limit+1):
                newtight = tight and digits[pos] == cur
                if prev == cur == 1:
                    res += dfs(pos+1,newtight,1,True)
                else:
                    res += dfs(pos+1,newtight,cur,repeated)
            return res

        return dfs(0,True,n[0],False)