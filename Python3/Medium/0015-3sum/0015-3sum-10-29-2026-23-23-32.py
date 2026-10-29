class Solution:
    def threeSum(self, nums: list[int]) -> list[list[int]]:
        nums.sort()
        res = []
        n = len(nums)
        for i in range(len(nums)-2):
            x = nums[i]
            if i and x == nums[i-1] or x + nums[i+1] + nums[i+2] > 0 or x + nums[-1] +nums[-2] < 0:
                continue
                
            j = i + 1
            k = n-1
            
            while j < k:
                s = nums[j] + nums[k] + x
                if s == 0:
                    res.append([x,nums[j],nums[k]])
                    j += 1
                    while j < k and nums[j] == nums[j-1]:
                        j += 1

                    k -= 1
                    while k > j and nums[k] == nums[k+1]:
                        k -= 1
                elif s > 0:
                    k -= 1
                else:   
                    j += 1
        return res
                
