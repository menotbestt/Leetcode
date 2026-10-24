class Solution:
    def permute(self, nums: list[int]) -> list[list[int]]:
        #Initialisation
        res = []
        path = []
        v = set()
        #DFS
        def dfs():
            if len(path) == len(nums): #Base Case
                res.append(path[:])
                return

            for i in nums: #Iteration
                if i in v:
                    continue
                
                path.append(i)
                v.add(i)
                dfs()
                v.remove(i)
                path.pop()

        dfs()
        return res