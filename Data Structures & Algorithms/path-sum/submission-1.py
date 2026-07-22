# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        if not root:
            return False
            
        def dfs(node, currSum):
            if not node.left and not node.right:
                if currSum == targetSum:
                    return True
                else:
                    return False

            if node.left or node.right:
                if node.left:
                    left = dfs(node.left, currSum + node.left.val)
                else:
                    left = False
                if node.right:
                    right = dfs(node.right, currSum + node.right.val)
                else:
                    right = False

            if right or left:
                return True
            else:
                return False

        return dfs(root, root.val)