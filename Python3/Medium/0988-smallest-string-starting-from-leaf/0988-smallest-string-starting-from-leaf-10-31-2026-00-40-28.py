class Solution:
    def smallestFromLeaf(self, root):
        path = []
        def dfs(node,cur):
            if not node:
                return
            c = chr(97+node.val) + cur
            if not node.left and not node.right:
                path.append(c)
                return
            dfs(node.left,c)
            dfs(node.right,c)
        dfs(root,'')
        return min(path)
