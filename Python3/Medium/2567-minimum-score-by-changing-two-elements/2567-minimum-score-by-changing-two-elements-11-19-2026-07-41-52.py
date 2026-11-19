class Solution:
    def minimizeSum(self, nums: List[int]) -> int:
        nums.sort()
        return min(b-a for a,b in zip(nums[:3],nums[-3:]))
