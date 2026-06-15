# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        q = deque()
        q.append(root)

        result = []
        while q:
            qlen = len(q)
            RightSide = None
            for i in range(qlen):
                node = q.popleft()
                if node:
                    RightSide = node
                    q.append(node.left)
                    q.append(node.right)

            if RightSide:
                result.append(RightSide.val)
                
        return result