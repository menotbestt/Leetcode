class Solution:
    def countDigitOne(self, n: int) -> int:
        nums = list(map(int,str(n)))
        L = len(nums)

        @cache
        def dfs(pos,tight):
            if pos == L:
                return (1,0)
            limit = nums[pos] if tight else 9
            total_count = 0
            total_ones = 0

            for cur in range(1+limit):
                newtight = tight and nums[pos] == cur
              
                cnt, ones = dfs(pos+1,newtight)
                total_count += cnt
                total_ones += ones

                if cur == 1:
                    total_ones += cnt
                    
            return total_count,total_ones
        return dfs(0,True)[1]
