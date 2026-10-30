class Solution:
    def letterCombinations(self, digits: str) -> list[str]:
        d={
            '2':'abc',
            '3':'def',
            '4':'ghi',
            '5':'jkl',
            '6':'mno',
            '7':'pqrs',
            '8':'tuv',
            '9':'wxyz'
        }
        res =[]
        def dfs(idx,comb):
            if idx == len(digits):
                res.append(comb[:])
                return
            
            for i in d[digits[idx]]:
                dfs(idx+1,comb + i)
        dfs(0,'')
        return res
            
        
