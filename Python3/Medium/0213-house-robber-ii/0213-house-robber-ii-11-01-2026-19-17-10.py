class Solution:
    def rob(self, nums: list[int]) -> int:
        if len(nums) <= 2:
            return max(nums)
        n = len(nums)
        def helper(num):
            dp = [0]*(n-1)
            dp[0] = num[0]
            dp[1] = max(num[0],num[1])
            for i in range(2,n-1):
                dp[i] = max(dp[i-1], dp[i-2] + num[i])

            return dp[-1]

        return max(helper(nums[1:]),helper(nums[:-1]))