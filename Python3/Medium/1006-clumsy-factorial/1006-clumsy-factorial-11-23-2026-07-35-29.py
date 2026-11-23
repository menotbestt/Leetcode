class Solution:
    def clumsy(self, n: int) -> int:
        s = ['*','//','+','-']
        rs = ''
        idx = 0
        for i in range(n,0,-1):
            temp = s[idx]
            rs += f"{i}{temp}"
            idx = (idx+1) % 4
        
        return eval(rs[:-2]) if idx == 2 else eval(rs[:-1])
