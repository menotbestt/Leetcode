class Solution:
    def numDupDigitsAtMostN(self,n: int) -> int:
        nums = list(map(int,str(n)))
        L = len(nums)
        @cache
        def dfs(pos,tight,mask,repeated,started):
            if pos == L:
                return 1 if repeated and started else 0
            res = 0
            limit = nums[pos] if tight else 9
            for cur in range(1+limit):
                nt = tight and nums[pos] == cur
                if not started and not cur:
                    res += dfs(pos+1,nt,mask,repeated,started)
                else:
                    newrepeated = True if mask & (1 << cur) or repeated else False
                    newmask = mask|(1 << cur)
                    res += dfs(pos+1,nt,newmask,newrepeated,True)
            return res
        return dfs(0,True,0,False,False)
