class MinStack(object):

    def __init__(self):
        """
        initialize your data structure here.
        """
        self.stack = []
        self.minStack = []

    def push(self, x):
        """
        :type x: int
        :rtype: void
        """
        self.stack.append(x)
        if len(self.minStack):
            self.minStack.append(min(self.minStack.pop(0),x))
        else:
            self.minStack.append(x)

    def pop(self):
        """
        :rtype: void
        """
        temp = self.stack.pop(0)
        if temp != self.minStack.pop(0): self.minStack.append(temp)
        

    def top(self):
        """
        :rtype: int
        """
        return self.stack[-1]

    def getMin(self):
        """
        :rtype: int
        """
        return self.minStack[-1]


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(x)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()