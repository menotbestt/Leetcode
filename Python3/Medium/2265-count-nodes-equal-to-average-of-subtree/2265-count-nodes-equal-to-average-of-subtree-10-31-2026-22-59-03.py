# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def averageOfSubtree(self, root: TreeNode) -> int:
        cnt = 0
        def dfs(node):
            nonlocal cnt
            if not node:
                return (0,0)
            
            ls,lc = dfs(node.left)
            rs,rc = dfs(node.right) #Postorder

            total = ls+rs+node.val

            n = lc+rc+1
            if total//n ==node.val:
                cnt += 1

            return (total,n)

        dfs(root) 
        return cnt