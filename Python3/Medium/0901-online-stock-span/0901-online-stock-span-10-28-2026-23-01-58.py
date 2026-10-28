class StockSpanner:

    def __init__(self):
        self.mst = []

    def next(self, p: int) -> int:
        mst = self.mst
        cur = 1
        while mst and mst[-1][0] <= p:
            cur += mst[-1][1]
            mst.pop()

        self.mst.append([p,cur])
        return cur
    

        


# Your StockSpanner object will be instantiated and called as such:
# obj = StockSpanner()
# param_1 = obj.next(price)