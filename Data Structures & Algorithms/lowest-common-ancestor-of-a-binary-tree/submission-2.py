# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        if not root:
            return root
        if p.val == root.val or q.val == root.val:
            return root

        res = TreeNode()
        

        def dfs(node):
            nonlocal res
            truep = False
            trueq = False

            if not node:
                if truep and trueq:
                    return True
                else:
                    return False

            if node.left and node.right:
                if node.left.val == p.val and node.right.val == q.val:
                    truep = True
                    trueq = True 
                    res.val = node.val
                    return True
                elif node.left.val == q.val and node.right.val == p.val:
                    truep = True
                    trueq = True 
                    res.val = node.val
                    return True
                    

            if node.val == p.val and not truep:
                truep = True
                trueq = dfs(node.left) or dfs(node.right)
                if truep and trueq:
                    res.val = node.val
                return True
            elif node.val == q.val and not trueq:
                trueq = True
                truep = dfs(node.left) or dfs(node.right)
                if trueq and truep:
                    res.val = node.val
                return True

            if not truep or not trueq:
                left = dfs(node.left)
                right = dfs(node.right)
            else:
                return False
            print(left, right)
            if left and right:
                print("root")
                res.val = node.val
                return True
            elif left or right:
                print("k")
                return True
            else:
                return False
        dfs(root)
        return res