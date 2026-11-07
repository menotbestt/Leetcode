class Solution:
    def countValidSubstrings(self, s: str) -> int:
        if 'abc' not in s:
            return len(s) * (len(s)+1) //2
        l = 0
        res=  0
        for r in range(len(s)):
            while r - l >= 2 and s[r-2] == 'a' and s[r-1] == 'b' and s[r] == 'c':
                l += 1
            res += r-l+1
            
        return res