class Solution:
    def allPathsSourceTarget(self, graph: list[list[int]]) -> list[list[int]]:
        path = []
        res = []
        
        def dfs(n):
            path.append(n)
            if n == len(graph)-1:
                res.append(path[:])
            else:
                for nei in graph[n]:
                    dfs(nei)
            path.pop()

        dfs(0)
        return res