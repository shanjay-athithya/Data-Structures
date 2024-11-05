class Foodqueue:
    def __init__(self, max):
        self.max = max
        self.rear = 0
        self.front = 0
        self.queue = [None] * self.max
        
    def position(self, position):
        return (position + 1) % self.max
    
    def isempty(self):
        if self.rear == self.front:
            return True
        return False
    
    def isfull(self):
        if self.front == self.position(self.rear):
            return True
        return False    
    def enqueue(self, ele):
        if not self.isfull():
            self.queue[self.rear] = ele
            self.rear += 1
        else:
            raise ValueError("the queue is full of orders")
    
    def dequeue(self):
        if not self.isempty():
            ele = self.queue[self.front]
            self.queue[self.front] = None
            self.front += 1
            return ele
        else:
            raise ValueError("no orders to deliever")
        
    def __str__(self):
        return str(self.queue)
        
if __name__ == "__main__":
    orders = Foodqueue(9)
    orders.enqueue("idly")
    orders.enqueue("sambar")
    orders.enqueue("pongal")
    print(orders)
    print(orders.dequeue())
    orders.enqueue("vada")
    print(orders)

    
    