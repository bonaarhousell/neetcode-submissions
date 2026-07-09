# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        dum = head
        mid = 0
        while dum:
            dum = dum.next
            mid += 1

        totalNext = 0
        if mid % 2 == 0:
            totalNext = (mid + 1) // 2
        else:
            totalNext = mid // 2

        while totalNext:
            head = head.next
            totalNext -= 1

        return head