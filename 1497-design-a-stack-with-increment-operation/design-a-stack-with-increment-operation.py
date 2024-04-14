class CustomStack:

    def __init__(self, maxSize: int):
        self.stack = []
        self.maxSize = maxSize
        self.currSize = 0

    def push(self, x: int) -> None:
        if self.currSize < self.maxSize:
            self.stack.append(x)
            self.currSize += 1

    def pop(self) -> int:
        x = -1
        if self.stack:
            x = self.stack.pop()
            self.currSize -= 1
        return x


    def increment(self, k: int, val: int) -> None:
        k = min(k, self.currSize)
        for i in range(k):
            self.stack[i] += val


# Your CustomStack object will be instantiated and called as such:
# obj = CustomStack(maxSize)
# obj.push(x)
# param_2 = obj.pop()
# obj.increment(k,val)