class Stack {
public:
    // Push element x onto stack.
    void push(int x) {
        self.queue.append(x)
    }

    // Removes the element on top of the stack.
    void pop() {
        for i in range(len(self.queue) -1):
            self.queue.append(self.queue.pop(0))
        return self.queue.pop(0)
    }

    // Get the top element.
    int top() {
        for i in range
    }

    // Return whether the stack is empty.
    bool empty() {
        
    }
};