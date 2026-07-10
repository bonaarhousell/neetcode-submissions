# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        if not head or not head.next:
            return head
        
        lengthList = 0
        dum = head
        while dum:
            lengthList += 1
            dum = dum.next
    
        k = k % lengthList
    
        cur = head
        while k:
            dum = head
            if not cur.next.next:
                dum = cur.next
                dum.next = head
                head = dum
                cur.next = None
                cur = dum
                k -= 1
            else:
                cur = cur.next

        return head