""" Online Stock Span """

class StockSpanner:

    def __init__(self):
        self.data = []
        

    def next(self, price: int) -> int:
        stock_span = 1
        while self.data and self.data[-1][0] <= price: 
            stock_span += self.data.pop()[1]
        self.data.append((price, stock_span))
        return stock_span         


# Your StockSpanner object will be instantiated and called as such:
# obj = StockSpanner()
# param_1 = obj.next(price)