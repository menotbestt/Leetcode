class Solution:
    def minChanges(self, s: str) -> int:
        return sum(1 for i in range(1,len(s),2) if s[i]!=s[i-1])