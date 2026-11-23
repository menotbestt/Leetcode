class ProductOfNumbers:
    def __init__(self):
        self.ps = [1]

    def add(self, num: int) -> None:
        if not num:
            self.ps = [1]
        else:
            self.ps.append(self.ps[-1] * num)
    def getProduct(self, k: int) -> int:
        if k >= len(self.ps):
            return 0
        return self.ps[-1] // self.ps[-k-1]

# Your ProductOfNumbers object will be instantiated and called as such:
# obj = ProductOfNumbers()
# obj.add(num)
# param_2 = obj.getProduct(k)