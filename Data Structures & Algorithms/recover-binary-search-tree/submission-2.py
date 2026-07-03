# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def recoverTree(self, root: Optional[TreeNode]) -> None:
        """
        Do not return anything, modify root in-place instead.
        """
        node1 = node2 = prev = None
        stack = []
        cur = root

        while stack or cur:
            while cur:
                stack.append(cur)
                cur = cur.left

            cur = stack.pop()
            if prev and prev.val > cur.val:
                node2 = cur
                if not node1:
                    node1 = prev
                else:
                    break
            
            prev = cur
            cur = cur.right

        node1.val, node2.val = node2.val, node1.val