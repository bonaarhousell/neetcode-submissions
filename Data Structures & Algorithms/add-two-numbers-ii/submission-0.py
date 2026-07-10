# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        sum1 = 0
        sum2 = 0

        sumNode = 0

        while l1:
            sum1 = sum1 * 10 + l1.val
            l1 = l1.next

        sumNode = 0
        while l2:
            sum2 = sum2 * 10 + l2.val
            l2 = l2.next

        buildList = sum1 + sum2
        buildList = str(buildList)
        cur = None
        res = cur
        for node in buildList:
            if not cur:
                cur = ListNode(int(node))
                res = cur
            else:
                cur.next = ListNode(int(node))
                cur = cur.next

        return res