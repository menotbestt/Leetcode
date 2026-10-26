class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        k = len(s1)
        tar = Counter(s1)
        d = Counter()
        for r in range(len(s2)):
            d[s2[r]] += 1 #Counter property
            if r >= k: #Moving forward
                d[s2[r-k]] -= 1
                if not d[s2[r-k]]:
                    del d[s2[r-k]]
                
            if r +1 >= k and d == tar: #r is index and k is len
                return True
    
        return False
