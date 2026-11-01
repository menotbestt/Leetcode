class Solution:
    def deleteAndEarn(self, nums: list[int]) -> int:
        s = [0] * (max(nums)+1)
        for i in nums:
            s[i] += i
        if len(s) <= 2:
            return max(s)
        dp = [0]*len(s)
        dp[0] = s[0]
        dp[1] = max(s[:2])
        for i in range(2,len(s)):
            dp[i] = max(dp[i-1],dp[i-2]+s[i])
        return dp[-1]
        