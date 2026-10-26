class Solution:
    def findAnagrams(self, s: str, p: str) -> list[int]:
        t = len(p)
        p = Counter(p)
        cur = Counter()
        res = []
        
        for r in range(len(s)):
            cur[s[r]] += 1
            if r >= t:
                cur[s[r-t]] -= 1 #If r surpasses the t we pop the leftmost item in window
                if not cur[s[r-t]]:
                    del cur[s[r-t]]
            
            if r + 1 >= t and p == cur:
                res.append(r-t+1) #return the first idx +1 becuase t is len and r is idx
        return res
