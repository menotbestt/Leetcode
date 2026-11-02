class Solution:
    def minMoves2(self, nums: list[int]) -> int:
        nums = sorted(nums)
        t = nums[len(nums)//2]
        return sum(abs(t-i) for i in nums)
