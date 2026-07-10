# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        if not head or not head.next:
            return head
        
        if k == 0:
            return head
        lengthList = 0
        dum = head
        while dum:
            lengthList += 1
            dum = dum.next
    
        k = k % lengthList
        newTailIdx = lengthList - k - 1

        cur = head
        while cur:
            if not cur.next:
                dum = head
                while newTailIdx:
                    newTailIdx-= 1
                    dum = dum.next
                cur.next = head
                head = dum.next
                dum.next = None
                break
            else:
                cur = cur.next
        return head