class Solution:
    def minMoves(self, nums: List[int]) -> int:
        return sum(max(nums)-i for i in nums)