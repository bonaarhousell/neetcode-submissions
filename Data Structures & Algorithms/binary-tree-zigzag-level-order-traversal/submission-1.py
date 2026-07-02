# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def zigzagLevelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        res = deque()

        def dfs(node, i, zigzag):
            if not node:
                return node

            nonlocal res
            if len(res) == i:
                res.append(deque())

            if zigzag:
                res[i].appendleft(node.val)
            else:
                res[i].append(node.val)
            
            if zigzag:
                dfs(node.right, i + 1, False)
                dfs(node.left, i + 1, False)
            else:
                dfs(node.right, i + 1, True)
                dfs(node.left, i + 1, True)

            return node

        dfs(root, 0, True)
       
        return list(res)
            