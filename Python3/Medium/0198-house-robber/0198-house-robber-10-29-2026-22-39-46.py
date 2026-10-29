class Solution:
    def rob(self, nums: list[int]) -> int:
        n = len(nums)
        @cache
        def dfs(i):
            if i < 0:
                return 0
            return max(dfs(i-1),dfs(i-2) + nums[i])
        
        return dfs(n-1)
