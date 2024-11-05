class Vector():
    """
    This class represents a mathematical vector.
    It can be initialized with a list of values or 
    an integer representing the dimension of the vector.
    """
    def __init__(self,val):
        if isinstance(val, list):
            self.cood = val
            self.dim = len(val)
        elif isinstance(val, int):
            self.cood = [0] * val
            self.dim = val
    #this function len is overwritten to return the len of the matrix
    def __len__(self):
        return len(self.cood)
    #this function setitem is overwritten to assign value to the index of the matrix
    def __setitem__(self, index, ele):
        self.cood[index] = ele
    #this function getitem is overwritten to return the element at index of the matrix
    def __getitem__(self, index):
        return self.cood[index]
    #this function eq is overwritten to check whether two vectors are equal
    def __eq__(self,other):
        return self.cood == other.cood
    def __add__(self,other):
        """
        Subtracts two vectors by subtracting their corresponding coordinates.
        """
        result = Vector(len(self.cood))
        #to perform vector addition the lenght of both vectors should be equal
        if len(self.cood) != len(other.cood):
            #an errror is raised if the length of both vectors are not equal
            raise ValueError("the two vectors are not in equal length")
        else:
            for i in range (len(self.cood)):
                #adding the elements of two vectors
                result.cood[i] = self.cood[i] + other.cood[i]
        return result.cood
    def __sub__(self,other):
        """
        Subtracts two vectors by subtracting their corresponding coordinates.
        """
        result = Vector(len(self.cood))
        #to perform vector subraction the lenght of both vectors should be equal
        if len(self.cood) != len(other.cood):
            #an errror is raised if the length of both vectors are not equal
            raise ValueError("the two vectors are not in equal length")
        else:
            for i in range (len(self.cood)):
                #subracting the elements of two vectors
                result.cood[i] = self.cood[i] - other.cood[i]
        return result.cood
    def __mul__(self,other):
        """
        Multiplies two vectors by multiplying their corresponding coordinates.
        """
        result = Vector(len(self.cood))
        #to perform vector multiplication the lenght of both vectors should be equal
        if len(self.cood) != len(other.cood):
            #an errror is raised if the length of both vectors are not equal
            raise ValueError("the two vectors are not in equal length")
        else:  
            for i in range (len(self.cood)):
                #multiplying the elements of two vectors
                result.cood[i] = self.cood[i] * other.cood[i]
        return result.cood
    def __truediv__(self,other):
        """
        Divides two vectors by dividing their corresponding coordinates.
        """
        result = Vector(len(self.cood))
        #to perform vector division the lenght of both vectors should be equal
        if len(self.cood) != len(other.cood):
            #an errror is raised if the length of both vectors are not equal
            raise ValueError("the two vectors are not in equal length")
        else:
            for i in range (len(self.cood)):
                #dividing the elements of two vectors
                result.cood[i] = self.cood[i] / other.cood[i]
        return result.cood
    def __str__(self):
        """
        Returns a string representation of the vector.
        """
        return str(self.cood)
if __name__ == '__main__':
    v1 = Vector(eval(input("enter the list of vector 1: ")))
    v2 = Vector(eval(input("enter the list of vector 2: ")))
    print(v1 + v2)#prints the sum of the vectors
    print(v1 - v2)#prints the subraction of the vectors
    print(v1 * v2)#prints the multiplication of the vectors
    print(v1 / v2)#prints the division of the vectors
    print(v1 == v2)#checks if the vectors are equal