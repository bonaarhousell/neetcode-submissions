class ListNode:
    def __init__(self, val="", next=None):
        self.val = val
        self.next = next

class Solution:

    def __init__(self):
        self.node = ListNode()

    def prefixCount(self, words: List[str], pref: str) -> int:
        if not pref:
            return 0
            
        node = self.node
        curr = node
        for p in pref:
            curr.next = ListNode(p)
            curr = curr.next

        word = "-" + "-".join(words)
        print(word)
        res = 0
        curr = node.next
        isFirstChar = False
        for char in word:
            if char == "-":
                isFirstChar = True
                continue
            if not curr and isFirstChar:
                curr = self.node.next
            if isFirstChar:
                if char == curr.val:
                    curr = curr.next
                    if not curr:
                        res += 1
                        isFirstChar = False
                else:
                    isFirstChar = False
                    curr = None
            

        return res  