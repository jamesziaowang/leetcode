class Queue(object):
    def __init__(self):
        """
        initialize your data structure here.
        """
        self.inStack = []
        self.outStack = []

    def push(self, x):
        """
        :type x: int
        :rtype: nothing
        """
        self.inStack.append(x)
        

    def pop(self):
        """
        :rtype: nothing
        """
        self.peed()
        self.outStack.pop(0)
        

    def peek(self):
        """
        :rtype: int
        """
        if not self.outStack:
            while self.inStack:
                self.outStack.append(self.inStack.pop())
        else:
            self.outStack[-1]

    def empty(self):
        """
        :rtype: bool
        """
        return len(self.outStack)+len(self.inStack) > 0