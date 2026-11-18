class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        start = []
        tar = word[0]
        R = len(board)
        C = len(board[0])
        for i in range(R):
            for j in range(C):
                if board[i][j] == tar:
                    start.append((i,j))
        v = set()           
        def dfs(r,c,idx):
            if idx == len(word):
                return True
            if (r,c) in v or r < 0 or c < 0 or r >= R or c >= C or board[r][c] != word[idx]:
                return False
            v.add((r,c))
            nidx = idx + 1
            for x,y in (0,1),(0,-1),(1,0),(-1,0):
                temp = dfs(r+x,c+y,nidx)
                if temp: return True
            v.remove((r,c))

        for r,c in start:
            if dfs(r,c,0):
                return True
        return False