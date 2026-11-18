class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        boardC = Counter(j for i in board for j in i)
        wordC = Counter(word)
        if wordC - boardC:
            return False
        if boardC[word[0]] < boardC[word[-1]]:
            word = word[::-1]
        
        start = []
        tar = word[0]
        R = len(board)
        C = len(board[0])
        for i in range(R):
            for j in range(C):
                if board[i][j] == tar:
                    start.append((i,j))
        def dfs(r,c,idx):
            if idx == len(word):
                return True
            if r < 0 or c < 0 or r >= R or c >= C or board[r][c] != word[idx]:
                return False
            nidx = idx + 1
            tempor = board[r][c]
            board[r][c] = '#'
            for x,y in (0,1),(0,-1),(1,0),(-1,0):
                temp = dfs(r+x,c+y,nidx)
                if temp: return True
            board[r][c] = tempor
            return False

        for r,c in start:
            if dfs(r,c,0):
                return True
        return False