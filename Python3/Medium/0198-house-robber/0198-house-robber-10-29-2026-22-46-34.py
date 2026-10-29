class Solution:
    def rob(self, nums: list[int]) -> int:
        dp = [0]*(2+len(nums))
        for i in range(len(nums)):
            dp[i+2] = max(dp[i+1], dp[i] + nums[i])
        return dp[-1]
