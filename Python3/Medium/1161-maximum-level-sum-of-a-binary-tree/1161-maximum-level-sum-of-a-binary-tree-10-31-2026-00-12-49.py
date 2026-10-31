# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxLevelSum(self, root: TreeNode | None) -> int:
        d = {}
        def dfs(node,lvl):
            nonlocal d
            if not node:
                return 
            if lvl in d:
                d[lvl] += node.val
            else:
                d[lvl] = node.val
            dfs(node.left,lvl+1)
            dfs(node.right,lvl+1)
        dfs(root,1)
        cur = 0
        m = -inf
        for i in d:
            if d[i] > m:
                cur = i
                m = d[i]
        return cur