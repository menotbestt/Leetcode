class Solution:
    def generateParenthesis(self, n: int) -> list[str]:
        res = []
        def dfs(cur:list,l,r):
            if n == l == r:
                res.append(''.join(cur))
                return
            if l > n:
                return
            
            if l < n:
                cur.append('(')
                dfs(cur , l+1, r)
                cur.pop()
             
            if r < l:
                cur.append(')')
                dfs(cur ,l, r+1)
                cur.pop()

           
        
        dfs([],0,0)

        return res
            
            
        