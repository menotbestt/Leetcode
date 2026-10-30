class Solution:
    def permute(self, nums: list[int]) -> list[list[int]]:
        res = []
        path =[]
        def dfs():
            if len(path) == len(nums):
                res.append(path[:])
            
            for i in nums:
                if i in path:
                    continue
                path.append(i)
                dfs()
                path.pop()
        dfs()
        return res