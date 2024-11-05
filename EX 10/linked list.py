from node import Node
class Singlyliinkedlist:
    """ 
    this class is used to create a single linked list where 
    we can perform append, find, display and length operations
    """
    def __init__(self):
        self.head = self.tail = Node()
        
    def append(self, ele):
        """ 
        This function is used to add elements to the linked list
        """
        n = Node(ele)
        self.tail.next = n
        self.tail = n
        
    def find(self, ele):
        """ 
        This function is used to check whether the element is present 
        in the linked queue if yes it returns its position address
        """
        pos = self.head.next
        while pos != None:
            if pos.data == ele:
                return pos
            pos = pos.next
        return -1
    
    def display(self):
        """ 
        This function is used to display the elements in the linked list
        """
        pos = self.head.next
        while pos is not  None:
            print(pos.data)
            pos = pos.next
            
    def insert(self, ind, ele):
        """
        This function is used to inside elements into the linked list
        """
        n = Node(ele)
        pos = self.head.next
        for i in range(ind - 1):
            pos = pos.next
        n.next = pos.next
        pos.next = n
        
    def previous(self, ele):
        """ 
        This function is used to find the address of the previous node
        """
        pos = self.head.next
        while pos is not None:
            if pos.next.data == ele:
                return pos
            pos = pos.next
        
    def remove(self, ele):
        """  
        This function is used to remove an element from the linked list
        """
        pos = self.previous(ele)
        pos.next = pos.next.next
            
if __name__ == "__main__":
    s = Singlyliinkedlist()
    s.append(2)
    s.append(3)
    s.append(4)
    s.append(8)
    s.insert(1,9)
    s.remove(3)
    d = s.display()
    d
    e = s.find(4)
    print(e.data)