import ctypes
class DualQueue:
    def __init__(self, cap):
        self.cap = cap
        self.rear1 = 0
        self.rear2 = cap - 1
        self.front1 = 0
        self.front2 = cap - 1
        self.queue = self.create_array(self.cap)
    
    def create_array(self, cap):
        return (cap * ctypes.py_object)()
    
    def __getitem__(self, index):
        return self.queue[index]
    
    def __setitem__(self, index, value):
        self.queue[index] = value
    
    def  isfull(self):
        if self.rear1 > self.rear2:
            return True
        return False
    
    def isempty(self):
        if self.rear1 == 0 and self.rear2 == self.cap - 1:
            return True
        return False
    
    def enqueue(self, queuenum, ele):
        if not self.isfull():
            if queuenum == 0:
                self.queue[self.rear1] = ele
                self.rear1 += 1
            elif queuenum == 1:
                self.queue[self.rear2] = ele
                self.rear2 -= 1
        else:
            raise ValueError ("the queue is full")
    
    def dequeue(self):
        if not self.rear1 == self.front1:
            ele = self.queue[self.front1]
            self.queue[self.front1] = None
            self.front1 += 1
            return ele
        else:
            ele = self.queue[self.front2]
            self.queue[self.front2] = None
            self.front2 -= 1
            return ele
        
    def __str__(self):
        a="["
        for i in range(self.rear1):
            a+=str(self.queue[i])
            
            a+=","
        for j in range(self.rear2 + 1,self.cap):
            a+=str(self.queue[j])
            if j!=self.cap-1:
                a+=","
        a+="]"
        return a
        
if __name__ == "__main__":
    dq = DualQueue(6)
    dq.enqueue(1,1)
    dq.enqueue(1,3)
    dq.enqueue(0,8)
    dq.enqueue(0,8)
    dq.enqueue(0,8)
    dq.enqueue(0,8)
    print(dq)
    print(dq.dequeue())
    print(dq.dequeue())
    print(dq.dequeue())
    print(dq.dequeue())
    print(dq.dequeue())
    print(dq)   