# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        if not root:return 

        res = 0
        def dfs(node,curm):
            nonlocal res
            if not node:
                return 0
            
            if node.val >= curm:
                res += 1
                curm = node.val
            if node.left:
                dfs(node.left,curm)
            if node.right:
                dfs(node.right,curm)
        dfs(root,-inf)
        return res