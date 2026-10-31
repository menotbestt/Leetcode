# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def binaryTreePaths(self, root: TreeNode | None) -> list[str]:
        res = []
        path = []
        #a nice backtracking problem i think
        def dfs(node):
            if not node:
                return 
            if not node.left and not node.right:
                return res.append(path+[str(node.val)])
            path.append(str(node.val))
            dfs(node.left)
            dfs(node.right)
            path.pop()
            
        dfs(root)
        
        return ['->'.join(i) for i in res]
