class Solution:
    def longestPalindrome(self, s: str) -> int:
        d = Counter(s)
        k = dict(d)
        res = 0
        for i in d:
            if d[i]%2:
                res += d[i]-1
            else:
                res += d[i]
                del k[i]

        return res+1 if k else res