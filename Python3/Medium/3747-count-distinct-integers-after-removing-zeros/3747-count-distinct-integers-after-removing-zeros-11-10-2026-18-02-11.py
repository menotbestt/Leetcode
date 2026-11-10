class Solution:
    def countDistinct(self, n: int) -> int:
        nums = list(map(int,str(n)))
        L = len(nums)
        @cache
        def dfs(pos,started,tight):
            if pos == L:
                return 1 if started else 0
            
            res = 0
            limit = nums[pos] if tight else 9
            for cur in range(1+limit):
                nt = tight and nums[pos] == cur
                
                if not cur and not started:
                    res += dfs(pos+1,False,nt)
                else:
                    if not cur:
                        continue
                    res += dfs(pos+1,True,nt)

            return res

        return dfs(0,False,True)