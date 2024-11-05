class Node:
    """ 
    This class is used to form a node
    """
    __slots__ = ['data','next']
    def __init__(self, data = None, next=None):
        self.data = data
        self.next = next
    
    
    