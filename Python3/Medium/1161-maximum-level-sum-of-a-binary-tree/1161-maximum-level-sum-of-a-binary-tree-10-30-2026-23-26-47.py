# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxLevelSum(self, root: TreeNode | None) -> int:
        q= deque([root])
        m = -inf
        idx = 1
        while q:
            lvl = len(q)
            
            temp = 0
            for _ in range(lvl):
                node = q.popleft()
                temp += node.val
                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)
            if temp > m:
                res = idx
                m = temp
            idx += 1

        return res