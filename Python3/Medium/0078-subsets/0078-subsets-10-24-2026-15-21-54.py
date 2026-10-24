class Solution:
    def subsets(self, nums: list[int]) -> list[list[int]]:
        #Exact same solution as combinations: Howevere there isnt't a 'k' restriction
        res = []
        path = []
        def dfs(s):
            res.append(path[:]) #Thus we do not need to validate the path length

            for i in range(s,len(nums)):
                path.append(nums[i])
                dfs(i+1)
                path.pop()

        dfs(0)
        return res
            
