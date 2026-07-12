class LinkedList:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class MyLinkedList:

    def __init__(self):
        self.node = LinkedList(0)

    def get(self, index: int) -> int:
        curr = self.node
        while index and curr:
            curr = curr.next
            index -= 1
            if not index and curr:
                return curr.val

        return -1

    def addAtHead(self, val: int) -> None:
        if self.node.val == 0:
            self.node.val = val
            print(self.node.val)
        else:
            prevHead = self.node
            newHead = LinkedList(val)
            newHead.next = prevHead
            self.node = newHead

    def addAtTail(self, val: int) -> None:
        curr = self.node
        while curr.next:
            curr = curr.next
        
        curr.next = LinkedList(val)
            
    def addAtIndex(self, index: int, val: int) -> None:
        curr = self.node
        while index and curr:
            index -= 1
            if not index and curr and curr.next:
                dum = curr.next
                curr.next = LinkedList(val)
                addNode = curr.next
                addNode.next = dum
            elif not index and curr and not curr.next:
                curr.next = LinkedList(val)
            curr = curr.next

    def deleteAtIndex(self, index: int) -> None:
        curr = self.node
        while index and curr:
            index -= 1
            if not index and curr and curr.next:
                dum = curr.next.next
                curr.next = None
                curr.next = dum
                return
            elif not index and curr and curr.next and not curr.next.next:
                curr.next = None
                return
            curr = curr.next


# Your MyLinkedList object will be instantiated and called as such:
# obj = MyLinkedList()
# param_1 = obj.get(index)
# obj.addAtHead(val)
# obj.addAtTail(val)
# obj.addAtIndex(index,val)
# obj.deleteAtIndex(index)