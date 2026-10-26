class BrowserHistory:
    def __init__(self, homepage: str):
        self.s = [homepage]
        self.cur = 0

    def visit(self, url: str) -> None:
        self.s = self.s[:self.cur+1]
        self.s.append(url)
        self.cur += 1

    def back(self, steps: int) -> str:
        self.cur = max(0,self.cur-steps)
        return self.s[self.cur]

    def forward(self, steps: int) -> str:
        self.cur = min(len(self.s)-1,self.cur+steps)
        return self.s[self.cur]

# Your BrowserHistory object will be instantiated and called as such:
# obj = BrowserHistory(homepage)
# obj.visit(url)
# param_2 = obj.back(steps)
# param_3 = obj.forward(steps)