import ctypes
class DualStack:
    """ 
    this class maintains two stack in an array
    """
    def __init__(self, cap):
        
        self.cap = cap
        self.top1 = 0
        self.top2 = self.cap - 1
        self.stack = self.create_array(self.cap)
        
    def create_array(self, cap):
        """
        Create and return an array of a given capacity using ctypes.
        An array of a given capacity."""
        return (cap * ctypes.py_object)()
    
    def __len__(self):
        """
        Return the total number of elements in the DualStack.
        The total number of elements in the DualStack.
        """
        return self.top2 - self.top1
    
    def __getitem__(self, index):
        """
        Get the element at the given index in the DualStack.
        index (int): The index of the element to retrieve.
        object: The element at the given index.
        """
        return self.stack[index]
    
    def __setitem__(self, index, value):
        """
        Set the element at the given index in the DualStack to the specified value.
        index (int): The index of the element to set.
        The value to set at the given index.
        """
        self.stack[index] = value
        
    def push(self, stacknum, ele):
        """
        Push an element onto the specified stack.
        The number of the stack (0 or 1) to push the element onto.
        The element to push onto the stack.
        Raises:
            ValueError: If the stack is full.
        """
        if not self.isfull() :
            if stacknum == 0:
                self.stack[self.top1] = ele
                self.top1 += 1
                
            elif stacknum == 1:
                self.stack[self.top2] = ele
                self.top2 -= 1
            
        else:
            raise ValueError("The stack is full")
        
    def pop(self, stacknum):
        """
        Pop an element from the specified stack.
        stacknum (int): The number of the stack (0 or 1) to pop the element from.
        Raises:
            ValueError: If the stack is empty.
        """
        if not self.isempty():
            if stacknum == 0:
                det = self.stack[self.top1 - 1]
                self.top1 -= 1
                return det
            elif stacknum == 1:
                det = self.stack[self.top2 + 1]
                self.top2 += 1
                return det
        else:
            raise ValueError("The stack is empty")
        
    def isfull(self):
        """
        Check if the DualStack is full.
        True if the DualStack is full, False otherwise.
        """
        if self.top1 > self.top2:
            return True
        return False
    
    def isempty(self):
        """
        Check if the DualStack is empty.
        True if the DualStack is empty, False otherwise.
        """
        if self.top1 == 0 and self.top2 == self.cap - 1:
            return True
        return False
            
    def __str__(self):
        a="["
        for i in range(self.top1):
            a+=str(self.stack[i])
            
            a+=","
        for j in range(self.top2+1,self.cap):
            a+=str(self.stack[j])
            if j!=self.cap-1:
                a+=","
        a+="]"
        return a

if __name__ == "__main__":
    ds = DualStack(5)
    ds.push(0, 1)
    ds.push(0, 3)
    ds.push(0, 0)
    ds.push(1, 8)
    ds.push(1, 9)
    print(ds.isempty())
    print(ds.isfull())
    print(ds)
    print(ds.pop(1))
    print(ds.pop(0))
