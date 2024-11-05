from random import randint
class Matrix():
    """
    this class creates a new matrix with
    the given dimensions of rows and columns
    """
    def __init__(self,r,c):#constructor
        self.row = r
        self.col = c
        self.mat = []
        #creating a matrix with the given dimensions
        for rows in range(r):
            l1 = [0] * c
            self.mat.append(l1)
    #a function to convert the resulting matrix to a string 
    def __str__(self):
        return str(self.mat)
    #rewriting getitem function to work also with matrices
    def __getitem__(self,index):
        return self.mat[index[0]][index[1]]
    #rewriting setitem function to work also with matrices
    def __setitem__(self,index,ele):
        self.mat[index[0]][index[1]] = ele
    #rewriting len function to return the len of matrices
    def __len__(self):
        return len(self.mat)
    def __add__(self,other):
        """
        this function is used to overwritre the add
        function to also work with matrices
        """
        #for adding two matrices their number of rows and columns must be equal.
        if len(self) != len(other) and len(self.mat[0]) != len(other.mat[0]):
            #raising an error to the user
            raise ValueError("the two vectors are not in equal length")
        else:
            #initiating the resultant matrix
            result = Matrix(len(self),len(self.mat[0]))
            for i in range(len(self)):
                for j in range(len(self.mat[0])):
                    #assigning the added elements of matrices to resultant matrix
                    result.mat[i][j] = self.mat[i][j] + other.mat[i][j]
            return result.mat
    def __sub__(self,other):
        """
        this function is used to overwritre the sub
        function to also work with matrices
        """
        #for subracting two matrices their number of rows and columns must be equal.
        if len(self) != len(other) and len(self.mat[0]) != len(other.mat[0]):
            #raising an error to the user
            raise ValueError("the two vectors are not in equal length")
        else:
            #initiating the resultant matrix
            result = Matrix(len(self),len(self.mat[0]))
            for i in range(len(self)):
                for j in range(len(self.mat[0])):
                    #assigning the subracted elements of matrices to resultant matrix
                    result.mat[i][j] = self.mat[i][j] - other.mat[i][j]
            return result.mat
    def __mul__(self,other):
        """
        this function is used to overwritre the mul
        function to also work with matrices
        """
        #for multiplying two matrices the row of second matrix and column of first matrix must be equal.
        if len(self.mat[0]) != len(other.mat):
            #raising an error to the user
            raise ValueError("the two vectors are not in equal length")
        else:
            result = Matrix(len(self.mat),len(other.mat[0]))
            for i in range(len(self.mat)):
                for j in range(len(other.mat[0])):
                    sum = 0
                    for k in range(len(other.mat)):
                        sum += self.mat[i][k] * other.mat[k][j]
                    result.mat[i][j] = sum
        return result.mat
    def determinant(self):
        """Creates a function that returns the determinant of the matrix 
        using the recursive function/...."""
        def getMinor(self,r,c):
            """
            This function returns the minor of the matrix m after removing the i-th row and j-th column.
            """
            return [row[:c] + row[c+1:] for row in (self[:r]+self[r+1:])]
        def getDeternminant(self):
            """
            This function calculates the determinant of the matrix m using recursion.
            """
            #the  condition for 2x2 matrix
            if len(self) == 2:
                return self[0][0] * self[1][1] - self[0][1] * self[1][0]
            determinant = 0
            for col in range(len(self)):
                determinant += ((-1) ** col) * self[0][col] * getDeternminant(getMinor(self,0,col))
            return determinant
        return getDeternminant(self.mat)
if __name__ == "__main__": 
    m1 = Matrix(3,3)
    m2 = Matrix(3,3)
    print("#test case 1") 
    print(m1[(1,2)])
    
    print("#test case 2")
    print(m1+m2)
    print(m1 - m2)
    
    print("#test case 3")
    print(m1 * m2)
    
    print("#test case 4")
    print(m1.determinant())
    
    print("#estcase 5")
    m3 = Matrix(3,2)
    m4 = Matrix(3,1)
    print(m3 * m4)
    print(m3.determinant())