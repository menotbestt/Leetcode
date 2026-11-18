# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sortedListToBST(self, head: ListNode | None) -> TreeNode | None:
        nums = []
        while head:
            nums.append(head.val)
            head = head.next
        
        def build(nums):
            if not nums:
                return
            mid = len(nums)//2
            cur = TreeNode(nums[mid])
            cur.left = build(nums[:mid])
            cur.right = build(nums[mid+1:])
            return cur
        return build(nums)