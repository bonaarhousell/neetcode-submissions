# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
        if left == right:
            return head
        leftList = []
        reverseList = []
        rightList = []

        cur = head
        seeLeft = False
        seeRight = False
        idxStartReverse = 1
        while cur:
            if idxStartReverse == left:
                seeLeft = True
                reverseList.append(cur.val)
                cur = cur.next
                idxStartReverse += 1
                continue
            elif idxStartReverse == right:
                seeRight = True
                reverseList.append(cur.val)
                cur = cur.next
                idxStartReverse += 1
                continue

            if seeLeft and not seeRight:
                reverseList.append(cur.val)
                cur = cur.next
            if not seeLeft:
                leftList.append(cur.val)
                cur = cur.next
            elif seeLeft and seeRight:
                rightList.append(cur.val)
                cur = cur.next
            idxStartReverse += 1

        print(leftList, reverseList, rightList)
        leftList = deque(leftList)
        reverseList.reverse()
        reverseList = deque(reverseList)
        rightList = deque(rightList)


        resHead = ListNode()
        if leftList:
            newHead = leftList.popleft()
            resHead.val = newHead
        else:
            newHead = reverseList.popleft()
            resHead.val = newHead
        curr = resHead
        while leftList or reverseList or rightList:
            if leftList:
                node = leftList.popleft()
                curr.next = ListNode(node)
                curr = curr.next
            elif reverseList:
                node = reverseList.popleft()
                curr.next = ListNode(node)
                curr = curr.next
            elif rightList:
                node = rightList.popleft()
                curr.next = ListNode(node)
                curr = curr.next
        
        return resHead
                
