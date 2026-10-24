class Solution:
    def subsets(self, nums: list[int]) -> list[list[int]]:
        res = []
        path = []
        def dfs(s):
            res.append(path[:])

            for i in range(s,len(nums)):
                path.append(nums[i])
                dfs(i+1)
                path.pop()

        dfs(0)
        return res
            
