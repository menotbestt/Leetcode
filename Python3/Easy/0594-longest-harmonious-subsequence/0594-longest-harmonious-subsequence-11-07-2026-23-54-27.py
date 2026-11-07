class Solution:
    def findLHS(self, nums: list[int]) -> int:
        d = SortedDict(Counter(nums))
        k = dict(d)
        print(d)
        last = inf
        m = 0
        for i in d:
            if last == inf:
                last = i
                continue
            if abs(last-i) == 1:
                m = max(d[last] + d[i], m)
            last = i
        return m
