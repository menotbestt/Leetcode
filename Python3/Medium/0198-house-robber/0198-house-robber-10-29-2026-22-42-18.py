class Solution:
    def rob(self, nums: list[int]) -> int:
        n = len(nums)
        cache = [-1]*n
        def dfs(i):
            if i < 0:
                return 0
            if cache[i] != -1:
                return cache[i]
            res =  max(dfs(i-1),dfs(i-2) + nums[i])
            cache[i] = res
            return res
        
        return dfs(n-1)
