class Solution:
    def permute(self, nums: list[int]) -> list[list[int]]:
        res =[]
        path=[]
        def dfs():
            if len(nums) == len(path):
                res.append(path[:])
                return
            
            for i in range(len(nums)):
                if nums[i] in path:
                    continue
                path.append(nums[i])
                dfs()
                path.pop()
        dfs()
        return res