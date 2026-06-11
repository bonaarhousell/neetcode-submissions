# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        if not p and not q:
            return True
        elif not p or not q:
            return False
        
        if p.val != q.val:
            return False
        stackp = [p]
        stackq= [q]

        while stackp and stackq:
            nodep = stackp.pop()
            nodeq = stackq.pop()

            if nodep.left or nodeq.left:
                if nodep.left == None:
                    return False
                elif nodeq.left == None:
                    return False
                if nodep.left.val == nodeq.left.val:
                     stackp.append(nodep.left)
                     stackq.append(nodeq.left)
                else:
                    return False
        
            if nodep.right or nodeq.right:
                if nodep.right == None:
                    return False
                elif nodeq.right == None:
                    return False
                if nodep.right.val == nodeq.right.val:
                     stackp.append(nodep.right)
                     stackq.append(nodeq.right)
                else:
                    return False
    

        return True