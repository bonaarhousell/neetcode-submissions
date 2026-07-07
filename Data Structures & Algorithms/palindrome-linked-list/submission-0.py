# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        stack = [head]
        
        res = []
        resReverse = []
        while stack:
            node = stack.pop()
            if not node:
                break
            res.append(node.val)
            resReverse.append(node.val)
            stack.append(node.next)

        resReverse.reverse()
        for r1, r2 in zip(res, resReverse):
            if r1 != r2:
                return False

        return True