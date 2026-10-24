class Solution:
    def solveNQueens(self, n: int) -> list[list[str]]:
        res = []
        path = []
        def dfs():
            if len(path) == n:
                temp = [['.']*n for i in range(n)]
                for r,c in path:
                    temp[r][c] = 'Q'
                res.append([''.join(i) for i in temp])
                return

            row = len(path)
            for col in range(n):
                conflict = False
                for r, c in path:
                    if col ==c or r-c == row-col or c+r == col+row :
                        conflict = True
                        break

                if conflict:
                    continue

                path.append((row, col))
                dfs()
                path.pop()

        dfs()
        return res