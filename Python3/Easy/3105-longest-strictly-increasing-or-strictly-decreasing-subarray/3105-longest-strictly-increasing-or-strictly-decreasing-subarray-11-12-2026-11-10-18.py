class Solution:
    def longestMonotonicSubarray(self, nums: List[int]) -> int:
        cnt = 1
        m = 1
        for i in range(1,len(nums)):
            if nums[i] >  nums[i-1]:
                cnt += 1
            else:
                m = max(m,cnt)
                cnt = 1
            m = max(cnt,m)

        cnt = 1
        m2 = 1
        for i in range(1,len(nums)):
            if nums[i] < nums[i-1]:
                cnt += 1
            else:
                m2 = max(m2,cnt)
                cnt = 1
            m2 = max(cnt,m2)
        return max(m2,m)
        

