class StockSpanner:

    def __init__(self):
        self.prices = []
        self.spans = []     

    def next(self, price: int) -> int:
        count = 1
        
        while self.prices and self.prices[-1] <= price:
            count += self.spans.pop()
            self.prices.pop()
        
        self.prices.append(price)
        self.spans.append(count)
        
        return count
    
# Your StockSpanner object will be instantiated and called as such:
# obj = StockSpanner()
# param_1 = obj.next(price)