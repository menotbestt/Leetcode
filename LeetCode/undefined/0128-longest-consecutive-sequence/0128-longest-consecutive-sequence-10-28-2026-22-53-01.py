class Solution:
    def longestConsecutive(self, nums: list[int]) -> int:
        num_set = set(nums)
        longest_streak = 0

            #2.遍历集合中的每一个数字
        for num in num_set:
            #3.核心灵魂：寻找排头兵
            #只有当num - 1不在集合时，才说明num是一段连续序列的起点
            if num - 1 not in num_set:
                current_num = num
                current_streak = 1

                #既然确认了自己是起点，就顺藤摸瓜往后找
                while current_num + 1 in num_set:
                    current_num += 1
                    current_streak += 1

                #更新历史最长纪录
                longest_streak = max(longest_streak, current_streak)

        return longest_streak
