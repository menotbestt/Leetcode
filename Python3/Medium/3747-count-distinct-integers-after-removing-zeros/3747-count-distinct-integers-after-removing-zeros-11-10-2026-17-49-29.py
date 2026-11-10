class Solution:
    def countDistinct(self, n: int) -> int:
        nums = list(map(int,str(n)))
        L = len(nums)
        @cache
        def dfs(pos,started,seen0,tight):
            if pos == L:
                return 1 if seen0 and started else 0
            
            res = 0
            limit = nums[pos] if tight else 9
            for cur in range(1+limit):
                nt = tight and nums[pos] == cur
                newseen0 = seen0 or (cur == 0 and started)
                ns = started or cur!=0
                res += dfs(pos+1,ns,newseen0,nt)
            return res

        return n - dfs(0,False,False,True)