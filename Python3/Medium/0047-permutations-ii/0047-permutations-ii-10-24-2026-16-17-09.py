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
                '''
                2 steps of checking
                1. if current node used already, skip
                2. if the same previous node is not used, we do not use it because the previous node isn't in path and we do not wish to repeat the same with current node
                We can only do this because we sorted nums already
                '''
                if used[i] or i > 0 and nums[i] == nums[i-1] and not used[i-1]: 
                    continue
                
                used[i] = True
                path.append(nums[i])

                dfs()

                path.pop()
                used[i] = False

        dfs()
        return res
