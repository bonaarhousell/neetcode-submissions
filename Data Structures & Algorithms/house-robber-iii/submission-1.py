# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rob(self, root: Optional[TreeNode]) -> int:
        def dfs(node):
            if not node:
                return [0, 0]

            leftpair = dfs(node.left)
            rightpair = dfs(node.right)

            withthief = node.val + leftpair[1] + rightpair[1]
            withoutthief = max(leftpair) + max(rightpair)

            return [withthief, withoutthief]

        return max(dfs(root))