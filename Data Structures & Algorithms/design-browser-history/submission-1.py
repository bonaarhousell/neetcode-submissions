class LinkedList:
    def __init__(self, val="", next=None, prev=None):
        self.val = val
        self.next = next
        self.prev = prev

class BrowserHistory:
    def __init__(self, homepage: str):
        self.homepage = homepage
        self.page = LinkedList(homepage)
        

    def visit(self, url: str) -> None:
        newPage = LinkedList(url)
        newPage.prev = self.page
        self.page.next = newPage
        self.page = self.page.next
        
        
    def back(self, steps: int) -> str:
        while steps:
            if not self.page.prev:
                return self.page.val
            self.page = self.page.prev
            steps -= 1

        return self.page.val
        

    def forward(self, steps: int) -> str:
        while steps:
            if not self.page.next:
                return self.page.val
            self.page = self.page.next
            steps -= 1
            
        return self.page.val


# Your BrowserHistory object will be instantiated and called as such:
# obj = BrowserHistory(homepage)
# obj.visit(url)
# param_2 = obj.back(steps)
# param_3 = obj.forward(steps)