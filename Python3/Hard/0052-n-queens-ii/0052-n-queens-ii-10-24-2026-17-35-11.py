class Solution:
    def totalNQueens(self, n: int) -> int:
        res = 0
        path = []
        def dfs():
            nonlocal res
            if len(path) == n:
                res += 1
                return
            
            row = len(path)
            for col in range(n):
                con = False
                for r,c in path:
                    if c == col or r+c == row + col or r-c == row - col:
                        con = True
                        break
                if con:
                    continue
                
                path.append((row,col))
                dfs()
                path.pop()
        dfs()
        return res