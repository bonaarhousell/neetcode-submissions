# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> Optional[ListNode]:
        if not intersectVal:
            return None
        lengthA, lengthB = 0, 0

        dumA, dumB = headA, headB
        while dumA or dumB:
            if not dumA:
                pass
            else:
                dumA = dumA.next
                lengthA += 1
            if not dumB:
                pass
            else:
                dumB = dumB.next
                lengthB += 1

        nodeA, nodeB = headA, headB
        while nodeA and nodeB:
            if lengthA > lengthB:
                nodeA = nodeA.next
                lengthA -= 1
            elif lengthB > lengthA:
                nodeB = nodeB.next
                lengthB -= 1
            else:
                nodeA = nodeA.next
                nodeB = nodeB.next
                lengthA -= 1
                lengthB -= 1
            
            if nodeA.val == intersectVal and nodeB.val == intersectVal:
                return nodeA