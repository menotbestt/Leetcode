class Solution:
    def minMoves(self, nums: list[int]) -> int:
        t = min(nums)
        r =0
        for i in nums:
            r += i - t
        return r