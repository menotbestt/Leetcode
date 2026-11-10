class Solution:
    def countDigitOne(self, n: int) -> int:
        nums = list(map(int,str(n)))
        L = len(nums)
        @cache
        def dfs(pos,total1,started,tight):
            if pos == L:
                return total1
            limit = nums[pos] if tight else 9
            res = 0
            for cur in range(1+limit):
                newstarted = started or cur != 0
                newtight = tight and nums[pos] == cur
                if cur == 1:
                    newtotal = total1 + 1
                else:
                    newtotal = total1

                res += dfs(pos+1,newtotal,newstarted,newtight)
            return res
        return dfs(0,False,False,True)

