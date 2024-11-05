from node import Node
class LinkedStack:
    """
    this class create a linked stack in which
    we can push and pop elements
    """
    def __init__(self):
        #forming a dummy node
        self.head = self.tail = Node()
        self.count = 0
        
    def isempty(self):
        """ 
        This function is used to find whether
        the stack is empty 
        """
        return self.head == self.tail
        
    def push(self, ele):
        """ 
        This function is used to push elements 
        into the linked stack
        """
        n = Node(ele)
        self.tail.next = n
        self.tail = n
        self.count += 1
        
    def pop(self):
        """ 
        This function is used to pop element from the 
        linked stack and return the element
        """
        if not self.isempty():
            #initializing the position
            pos = self.head
            while pos.next is not self.tail:
                pos = pos.next
            popele = self.tail.data
            pos.next = None
            self.tail = pos
            self.count -= 1
            return popele
        
        else:
            raise ValueError("the linked stack is empty")
        
    def display(self):
        """" 
        This function is used to display the  
        elements in the linked stack
        """
        pos = self.head.next
        while pos is not None:
            print(pos.data)
            pos = pos.next
            
    def __str__(self):
        """ 
        Overwriting the STR function to print the linked stack
        """
        a = '['
        pos = self.head.next
        while pos is not None:
            a = a + str(pos.data) + ','
            pos = pos.next
        a = a + ']'
        return a
    
    def __len__(self):
        '''This function is used to return 
        the length of the linked stack'''
        return self.count

if __name__ == '__main__':
    stack = LinkedStack()
    stack.push(0)
    stack.push(1)
    print(stack) 
    stack.display()
    print(len(stack)) 
    stack.pop()
    stack.pop() 
    print(stack)
       
        
        
        
             
        