class Solution:
    def permute(self, nums: list[int]) -> list[list[int]]:
        return list(map(list,itertools.permutations(nums,len(nums))))