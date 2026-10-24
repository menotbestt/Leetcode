class Solution:
    def permuteUnique(self, nums: list[int]) -> list[list[int]]:
        res = []
        path = []
        nums.sort()
        used = [False]*len(nums)
        def dfs():
            if len(path) == len(nums):
                res.append(path[:])
                return
            
            for i in range(len(nums)):
                if used[i] or i > 0 and nums[i] == nums[i-1] and not used[i-1]:
                    continue

                used[i] = True
                path.append(nums[i])

                dfs()

                path.pop()
                used[i] = False

        dfs()
        return res
