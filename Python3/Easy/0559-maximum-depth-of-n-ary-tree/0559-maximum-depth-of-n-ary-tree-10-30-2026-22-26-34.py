"""
# Definition for a Node.
class Node:
    def __init__(self, val: Optional[int] = None, children: Optional[List['Node']] = None):
        self.val = val
        self.children = children
"""

class Solution:
    def maxDepth(self, root: 'Node') -> int:
        
        res = 0
        def dfs(node):
            if not node:
                return 0 
            m = 0
            for i in node.children:
                m = max(dfs(i),m)
            return 1 + m

        res = dfs(root)
        return res
