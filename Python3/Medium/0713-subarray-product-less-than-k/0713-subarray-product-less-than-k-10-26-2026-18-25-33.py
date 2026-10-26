class Solution:
    def numSubarrayProductLessThanK(self, nums: list[int], k: int) -> int:
        if k<= 1:
            return 0
        cur = 1
        m = 0
        l = 0
        for r in range(len(nums)):
            cur *= nums[r]

            while cur >= k:
                cur //= nums[l]
                l += 1
            
            m += r-l+1
        return m