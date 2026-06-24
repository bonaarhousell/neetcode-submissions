# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rob(self, root: Optional[TreeNode]) -> int:
        res = {None: 0}
        def dfs(node):
            if node in res:
                return res[node]

            res[node] = node.val
            if node.left:
                res[node] += dfs(node.left.left) + dfs(node.left.right)
            if node.right:
                res[node] += dfs(node.right.left) + dfs(node.right.right)
            
            res[node] = max(res[node], dfs(node.left) + dfs(node.right))
            return res[node]

        return dfs(root)