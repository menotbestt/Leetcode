class Solution:
    def permute(self, nums: list[int]) -> list[list[int]]:
        res = []
        def dfs(path):
            if len(path) == len(nums):
                res.append(path)
                return
            
            for i in nums:
                if i in path:
                    continue
                dfs(path + [i])
                
        dfs([])
        return res