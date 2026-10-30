"""
# Definition for a Node.
class Node:
    def __init__(self, val: Optional[int] = None, children: Optional[List['Node']] = None):
        self.val = val
        self.children = children
"""

class Solution:
    def levelOrder(self, root: 'Node') -> List[List[int]]:
        if not root:
            return []
        q = deque([root])
        res = []
        while q:
            level = len(q) #Number of nodes to traverse per layer
            temp = []
            for i in range(level):
                node = q.popleft()
                temp.append(node.val) #BFS
                for i in node.children:
                    q.append(i)
            res.append(temp)

        return res
