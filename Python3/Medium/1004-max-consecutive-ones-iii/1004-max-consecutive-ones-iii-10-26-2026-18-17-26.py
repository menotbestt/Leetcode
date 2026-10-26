class Solution:
    def longestOnes(self, nums: list[int], k: int) -> int:
        zeros = 0
        m = 0
        cur = 0
        l = 0
        for r in range(len(nums)):
            if nums[r] == 0:
                zeros += 1

            while zeros > k:
                if not nums[l]:
                    zeros -= 1
                l += 1
            
            m = max(m,r-l + 1)
        return m
                