class Point():
    """
    this point class assigns the given values of point
    coordinates to the variables x and y coordinates
    """
    #a function called constructor is invoked due to object formation
    def __init__ (self, a, b):
        self.x = a
        self.y = b
    #defining a function to find the distance between the points
    def distance(self, other):
        #applying distance formula 
        x_diff = (self.x - other.x) ** 2
        y_diff = (self.y - other.y) ** 2
        dis_btw = (x_diff + y_diff) ** 0.5
        #returning distanve value
        return dis_btw
if __name__ == '__main__':
    #getting the input points from user    
    point_1 = Point(int((input("enter the x coordinate of point 1: "))), int((input("enter the y coordinate of point 1: "))))
    point_2 = Point(int((input("enter the x coordinate of point 2: "))), int((input("enter the y coordinate of point 2: "))))
    #displaying the output
    print(point_1.distance(point_2))