class Solution:
    def count(self, num1: str, num2: str, min_sum: int, max_sum: int) -> int:
        MOD = 10**9 + 7
        def solve(n):
            digits = list(map(int,n))
            L = len(digits)
            @cache
            def dfs(pos,tight,cursum):
                if cursum > max_sum:
                    return 0
                if pos == L:
                    return 1 if min_sum <= cursum <= max_sum else 0

                limit = digits[pos] if tight else 9
                res = 0
                for cur in range(1+limit):
                    nt = tight and digits[pos] == cur
                    newcursum = cursum + cur
                    res += dfs(pos+1, nt, newcursum)
                return res
            return dfs(0,True,0)

        return (solve(num2) - solve(str(int(num1)-1)))%MOD