class Stack:
    def __init__(self):
        self.size = 5
        self.q = list(range(self.size))
        self.index = 0
    def is_full(self):
        if self.index == self.size:return True
        return False
    def is_empty(self):
        if self.index == 0: return True
        return False
    def push(self, value):
        if self.is_full():
            print('Stack is Full, cannot Push')
            return
        self.q[self.index] = value
        self.index += 1
    def pop(self):
        if self.is_empty():
            print('Stack is empty, cannot pop')
            return
        self.index -= 1
        return self.q[self.index]
    
s = Stack()
s.push(1)
s.push(2)
print(s.pop())
print(s.pop())

        
        
