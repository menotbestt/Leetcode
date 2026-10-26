class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        k = len(s1)
        tar = Counter(s1)
        d = Counter()
        for r in range(len(s2)):
            d[s2[r]] += 1
            if r >= k:
                d[s2[r-k]] -= 1
                if not d[s2[r-k]]:
                    del d[s2[r-k]]
                
            if r - k >= -1 and d == tar:
                return True
    
        return False
