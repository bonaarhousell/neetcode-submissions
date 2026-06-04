# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        count1 = []
        count2 = []
        while l1 or l2:
            if l1:
                count1.append(str(l1.val))
                l1 = l1.next
            if l2:
                count2.append(str(l2.val))
                l2 = l2.next


        cnt1 = "".join(count1)
        cnt2 = "".join(count2)

        print(cnt1, cnt2)

        cnt1 = cnt1[::-1]
        cnt2 = cnt2[::-1]
        print(cnt1,cnt2)
        cnt1 = int(cnt1)
        cnt2 = int(cnt2)
        print(cnt1,cnt2)
        
        dum = [] 
        dum.append(cnt1 + cnt2)
        count = []
        for d in str(dum[0]):
            print(d)
            count.append(int(d))
        print(count)
        res = ListNode()
        c1 = res
        while count:
            cur = ListNode(count.pop())
            c1.next = cur
            c1 = c1.next

        return res.next

