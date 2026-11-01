class Solution:
    def lengthOfLIS(self, nums: list[int]) -> int:
        
        arr = []
        for n in nums:
            i = bisect_left(arr, n)
            if i < len(arr):
                arr[i] = n
            else:
                arr.append(n)
        return len(arr)
