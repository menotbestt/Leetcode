class Solution:
    def twoSum(self, n: list[int], t: int) -> list[int]:
        d = {}
        for i in range(len(n)):
            if t-n[i] in d:
                return d[t-n[i]],i
            d[n[i]] = i
