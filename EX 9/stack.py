class Stack:
    """
    this class is used to create a 
    stack data type using wrapper method
    """
    def __init__(self):
        """Initialize an empty stack."""
        self.seq = []

    def push(self, ele):
        """Push an element onto the stack."""
        self.seq.append(ele)

    def pop(self):
        """Remove and return the top element from the stack."""
        return self.seq.pop()

    def isempty(self):
        """Check if the stack is empty."""
        return len(self.seq) == 0

    def __str__(self):
        """Return a string representation of the stack."""
        return str(self.seq)


class Queue:
    """
    this class is used to create a 
    queue data type using wrapper method
    """
    def __init__(self):
        """Initialize an empty queue."""
        self.seq = []

    def enqueue(self, ele):
        """Add an element to the end of the queue."""
        self.seq.append(ele)

    def dequeue(self):
        """Remove and return the element at the front of the queue."""
        if not self.isempty():
            return self.seq.pop(0)

    def isempty(self):
        """Check if the queue is empty."""
        return len(self.seq) == 0

    def __str__(self):
        """Return a string representation of the queue."""
        return str(self.seq)


def palindrome(n):
    """Check if a number is a palindrome."""
    num = str(n)
    stack = Stack()
    queue = Queue()
    for digit in num:
        stack.push(digit)
        queue.enqueue(digit)
    while not stack.isempty():
        if stack.pop() != queue.dequeue():
            return False
    return True

if __name__ == "__main__":
    n = int(input("Enter a number: "))
    if palindrome(n) == True:
        print("the number is a palindrome")
    else:
        print("the number is not a palindrome")