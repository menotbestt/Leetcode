class Solution:
    def maximumSubarraySum(self, nums: List[int], k: int) -> int:
        seen = set()
        m = 0
        l = 0
        cur = m + 0
        for r in range(len(nums)):
            while nums[r] in seen:
                seen.remove(nums[l])
                cur -= nums[l]
                l += 1

            seen.add(nums[r])
            cur += nums[r]

            if r-l+1 == k:
                m = max(m,cur)
                seen.remove(nums[l])
                cur -= nums[l]
                l += 1

        return m

            
            