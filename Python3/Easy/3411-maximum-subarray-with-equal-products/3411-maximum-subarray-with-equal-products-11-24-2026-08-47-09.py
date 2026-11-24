class Solution:
    def maxLength(self, nums: List[int]) -> int:
        s = [nums[i : j + 1] for i in range(len(nums)) for j in range(i, len(nums))]
        m = 0
        for i in s:
            if prod(i) == lcm(*i) * gcd(*i):
                m = max(m,len(i))
        return m