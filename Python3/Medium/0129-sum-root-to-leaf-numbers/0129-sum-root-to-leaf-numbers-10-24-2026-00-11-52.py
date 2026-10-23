# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumNumbers(self, root: TreeNode | None) -> int:
        s = 0
        path = 0

        def dfs(n):
            if not n:
                return 
            nonlocal path,s
            path = path*10 + n.val
            if not n.left and not n.right:
                s += path
                path//=10
                return
            dfs(n.left)
            dfs(n.right)
            path //= 10

        dfs(root)
        return s
                

        