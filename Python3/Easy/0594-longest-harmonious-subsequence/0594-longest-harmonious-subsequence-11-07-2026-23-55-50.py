class Solution:
    def findLHS(self, nums: list[int]) -> int:
        d = Counter(nums)
        m = 0
        for i in d:
            if i+1 in d:
                m = max(d[i+1] + d[i], m)
        return m
