# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        #find the middle of linked list
        slow = head
        fast = head.next
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        #reversed the second linked list
        second = slow.next
        prev = slow.next = None
        while second:
            tmp = second.next
            second.next = prev
            prev = second
            second = tmp

        #stitch two of the linked list(head=first, prev=second)
        first, second = head, prev
        while second:
            tmp1, tmp2 = first.next, second.next
            first.next = second
            second.next = tmp1
            first,second = tmp1, tmp2

    #t1=1,2,3,none. t2=5,4,none. f=0,6,5,4,none, h=0,6,5,4,none. 
    #s=6,1,2,3,none, h=0,6,1,2,3,none. f=1,2,3,none. s=5,4,none.

    #t1=2,3,none. t2=4,none. f=1,5,4,none, h=0,6,1,5,4,none.
    #s=5,2,3,none, h=0,6,1,5,2,3,none. f=2,3,none. s=4,none.

    #t1=3,none. t2=none. f=2,4,none, h=0,6,1,5,2,4,none.
    #s=4,3,none, h=0,6,1,5,2,4,3,none. f=3,none. s=none.