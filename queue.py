class Queue:
    def __init__(self):
        self.size = 5
        self.q = list(range(self.size))
        self.i = 0
        self.o = 0
        self.is_empty = True
        self.is_full = False
        
    def inc(self, i):
        if i + 1 == self.size: i = 0
        else: i += 1
        return i
            
    def Enqueue(self, value):
        if self.is_full :
            print('Queue is full Cannot enqueue')
            return
        self.q[self.i] = value
        self.i = self.inc(self.i)
        if self.i == self.o :
            self.is_full = True
        self.is_empty = False
    def Dequeue(self):
        if self.is_empty:
            print('Queue is Empty, cannot dequeue')
            return
        retVal = self.q[self.o]
        self.o = self.inc(self.o)
        
        if self.i == self.o : self.is_empty = True
        self.is_full = False
        return retVal
    
obj = Queue()
obj.Enqueue(1)
obj.Enqueue(2)
obj.Enqueue(3)
obj.Enqueue(4)
print(obj.Dequeue())
print(obj.Dequeue())
obj.Enqueue(23)
obj.Enqueue(14)
print(obj.Dequeue())
print(obj.Dequeue())
print(obj.Dequeue())
print(obj.Dequeue())


