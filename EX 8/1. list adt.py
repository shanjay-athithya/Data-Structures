import ctypes
class DynamicArray():
    """
    this class is used to represent
    a dynamic array and enables us to 
    perform list operations
    """
    def __init__(self,val):
        #checks whether the value is an integer
        if isinstance(val, int):
            self.n = 0
            self.capacity = val
            self.A = self.createarray(self.capacity)
        #checks whether the value is a list
        if isinstance(val, list):
            self.n = len(val)
            self.capacity = len(val)
            self.A = val

    def createarray(self, cap):
        """
        this function is used to create a 
        new list double that of old list if there is 
        no capacity to add elements to the old list
        """
        array = (cap * ctypes.py_object)()
        return array

    def expand(self, capacity):
        """ 
        this function is used to expand
        the capacity of the list
        """
        B = self.createarray(capacity)
        for i in range(self.n):
            B[i] = self.A[i]
        self.A = B
        #assigning new capacity
        self.capacity = capacity

    def append(self, ele):
        """ 
        this function is used to append
        elements to the list
        """
        if self.n == self.capacity:
            self.expand(self.capacity * 2)
        self.A[self.n] = ele
        self.n+= 1

    def __len__(self):
        """ 
        this function is used to find the length
        of the list
        """
        return self.n

    def __getitem__(self, ind):
        """ 
        this function is used to retrive elements
        from the list if it is present
        """
        #checks whether the give index is within range
        if 0 <= ind < self.n:
            return self.A[ind]
        #raising error if the index is not within range
        raise IndexError ("index out of range")

    def __setitem__(self, ind, ele):
        """ 
        this function is used to assign element
        to the given index
        """
        #checks whether the give index is within range
        if 0 <= ind < self.n:
            self.A[ind] = ele
        else:
            #raising error if the index is not within range
            raise IndexError ("index out of range")
    
    def insert(self, index, ele):
        """ 
        this fuunction is used to insert an
        element to the particular index
        """
        #checks whether the give index is within range
        if 0 <= index < self.n + 1:
            #checks whether there is no space to insert
            if self.n == self.capacity:
                #expanding the capacity if no space in the list
                self.expand(self.capacity * 2)
            #giving space for the element to insert in the index
            for i in range(self.n-1, index - 1, -1):
                self.A[i+1] = self.A[i]
            self.A[index] = ele
            #incrementting the no of elements
            self.n += 1
        else:
            #raising error if the index is not within range
            raise IndexError ("index out of range")
    
    def delete(self, index):
        #checks whether the give index is within range
        if 0 <= index < self.n:
            #rearranging the elements in the list leaving the delete index
            for i in range(index, self.n-1):
                self.A[i] = self.A[i +1]
            self.n = self.n - 1
            #if the number of elements in the list is less than one fourth of capacity reducing the capacity by half
            if self.capacity // 4 >= self.n:
                self.expand(self.capacity // 2)
        else:
            #raising error if the index is not within range
            raise IndexError ("index out of range")

    def extend(self, exl):
        """ 
        this fuunctiion is used to extend the list by adding new list to it
        """
        for ele in exl:
            self.append(ele)
    
    def __contains__(self, ele):
        """ 
        this function is used to check if 
        whether an element is present in the list
        """
        for i in range(self.n):
            if self.A[i] == ele:
                #returning true if the element is present
                return True
        else:
            #returning false if the element is not present
            return False
    
    def index(self, ele):
        """ 
        this function is used to find the index 
        of an element in the list
        """
        for i in range(self.n):
            #checking whether the element is present
            if self.A[i] == ele:
                #returning index if the element is present
                return i
        else:
            #returning None if the element is not present
            return None
    def count(self, ele):
        """
        this function is used to find number of 
        times the element is present in the list
        """
        c = 0
        for i in range(self.n):
            #checking if the element is present
            if self.A[i] == ele:
                #incrementing if the element is present
                c += 1
        if c == 0:
            return "element not found"
        else:
            return c
    
    def __str__(self):
        """ 
        this function is used to print the
        list as string instead of memeory address
        """
        return str(list(self.A[:self.n]))

if __name__ == "__main__":
    b = [1, 2, 3, 4, 5, 6]
    a = DynamicArray(b)
    a.extend([9,8,7,0,6])
    #initial list
    print(list(a[i] for i in range(len(a))))
    print("--------------------------------")
    print(a.count(6))
    print("--------------------------------")
    print(a.index(100))
    print("--------------------------------")
    print(a[10])
    print("--------------------------------")
    a.delete(0)
    a.insert(2,999)
    print(0 in a)
    print("--------------------------------")
    print(len(a))
    print("--------------------------------")
    #updated list
    print(list(a[i] for i in range(len(a))))
    