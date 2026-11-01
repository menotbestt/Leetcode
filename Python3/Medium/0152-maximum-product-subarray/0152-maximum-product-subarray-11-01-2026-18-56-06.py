class Solution:
    def maxProduct(self, nums: list[int]) -> int:
        n = len(nums)
        dp1 = [0]*n
        dp2 = [0]*n
        dp1[0] = dp2[0] = nums[0]
        for i in range(1,len(nums)):
            x = nums[i]
            dp1[i] = max(x,x*dp1[i-1],x*dp2[i-1])
            dp2[i] = min(x,x*dp1[i-1],x*dp2[i-1])

        return max(dp1)