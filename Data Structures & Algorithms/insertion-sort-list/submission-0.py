# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def insertionSortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        sortNode = []

        dum = head
        while dum:
            sortNode.append(dum.val)
            dum = dum.next


        sortNode.sort()
        sortNode = deque(sortNode)

        newHead = ListNode(sortNode.popleft())
        resHead = newHead
        while sortNode:
            node = sortNode.popleft()
            newHead.next = ListNode(node)
            newHead = newHead.next

        return resHead
