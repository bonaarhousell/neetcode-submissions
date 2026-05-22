class StockSpanner:

    def __init__(self):
        self.scanner = []

    def next(self, price: int) -> int:
        count = 1
        while self.scanner and self.scanner[-1][0] <= price:
            count += self.scanner[-1][1]
            self.scanner.pop() 
        self.scanner.append((price, count))
        return count
        
# Your StockSpanner object will be instantiated and called as such:
# obj = StockSpanner()
# param_1 = obj.next(price)