# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeElements(self, head: Optional[ListNode], val: int) -> Optional[ListNode]:
        if not head:
            return head
        node = head
        cur = head
        while node:
            if node.next and node.next.val == val:
                cur = node.next.next
                node.next = cur
            else:
                node = node.next 
            
        if head.val == val:
            head = head.next
        return head