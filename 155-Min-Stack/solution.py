class MinStack(object):

    # @param x, an integer
    # @return an integer
    def __init__(self):
        self.nodes = [] #元素栈
        self.minNodes = [] #最小值栈

    def push(self, x):
        self.nodes.append(x)
        if len(self.minNodes):
            x = min(self.minNodes[-1], x)
        self.minNodes.append(x)

    def pop(self):
        self.minNodes.pop()
        return self.nodes.pop()

    def top(self):
        return self.nodes[-1]

    def getMin(self):
        return self.minNodes[-1]


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(x)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()