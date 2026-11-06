class Solution:
    def getRow(self, n: int) -> list[int]:
        return  [comb(n, k) for k in range(n+1)]