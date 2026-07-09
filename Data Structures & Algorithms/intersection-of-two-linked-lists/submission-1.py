# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> Optional[ListNode]:

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
                if nodeA == nodeB:
                    return nodeA
                nodeA = nodeA.next
                nodeB = nodeB.next
                lengthA -= 1
                lengthB -= 1
            
