"""
# Definition for a Node.
class Node:
    def __init__(self, val: Optional[int] = None, children: Optional[List['Node']] = None):
        self.val = val
        self.children = children
"""

class Solution:
    def postorder(self, root: 'Node') -> List[int]:
        if not root:
            return []
        
        if not root.children:
            return [root.val]

        res = []
        for i in root.children:
            res += self.postorder(i)
        res.append(root.val)
        return res