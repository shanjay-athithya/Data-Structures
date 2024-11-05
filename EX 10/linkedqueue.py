from node import Node
class LinkedQueue:
    """  
    This class is used to do form linked queues 
    and perform NQ&DQ operations
    """
    def __init__(self):
        #a dummy header is formed
        self.front = self.rear = Node()
        self.count = 0
    def isempty(self):
        """ 
        This function checks whether the Queue is empty or not
        """
        return self.front == self.rear
    def enqueue(self, ele):
        """ 
        This function is used to NQ the 
        elements to the linked queue
        """
        n = Node(ele)
        self.rear.next = n
        self.rear = n
        self.count += 1
        
    def dequeue(self):
        """ 
        This function is used to dequeue the element 
        from the linked queue and return the element
        """
        if not self.isempty():
            delnode = self.front.next
            delele = delnode.data
            self.front.next = delnode.next
            self.count -= 1
            return delele
        else:
            raise ValueError("the linked queue is empty")
    def __len__(self):
        """ 
        This function returns the length of the linked Overrating the STR function to print the linked queue
        """
        return self.count
    def display(self):
        """ 
        This function is used to do display the elements in the linked queue
        """
        pos = self.front.next
        while pos is not None:
            print(pos.data)
            pos = pos.next
            
    def __str__(self):
        """ 
        Overrating the STR function to print the linked queue
        """
        a = '['
        pos = self.front.next
        while pos is not None:
            a = a + str(pos.data) + ','
            pos = pos.next
        a = a + ']'
        return a
    
if __name__ == '__main__':
    q = LinkedQueue()
    q.enqueue(7)
    q.enqueue(1)
    q.enqueue(8)
    print(q.dequeue())
    print(q)
    print(len(q))
    q.enqueue(0)
    q.enqueue()
    
        