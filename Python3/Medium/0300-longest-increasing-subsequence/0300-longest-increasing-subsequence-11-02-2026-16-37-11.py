class Solution:
    def lengthOfLIS(self, nums: list[int]) -> int:
        res = [nums[0]]
        for i in nums[1:]:
            if i > res[-1]:
                res.append(i)
            else:
                temp = bisect_left(res,i)
                if temp < len(res):
                    res[temp] = i
        return len(res)
        
            