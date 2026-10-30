# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findTilt(self, root: Optional[TreeNode]) -> int:
        s = 0
        def dfs(n):
            nonlocal s
            if not n:
                return 0
            l = dfs(n.left)
            r = dfs(n.right)
            s += abs(l-r)
            return n.val + l + r
        dfs(root)
        return s

            