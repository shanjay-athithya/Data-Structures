class Point():
    """
    creating a class point that assigns
    the given points into their respective x and y vcoordinatess
    """
    #constructor function is invoked due to object formation
    def __init__ (self, a, b):
        self.x = a
        self.y = b
    #defining a function to find the distance between the points
    def distance(self, other):
        x_diff = (self.x - other.x) ** 2
        y_diff = (self.y - other.y) ** 2
        dis_btw = (x_diff + y_diff) ** 0.5
        #returning distance value
        return dis_btw
#defing  a funtion to generate random points
def rand_list(ran):
    """
    this video randomly generates a sequence
    of points and stores in a list
    """
    list = []
    import random
    for i in range (ran):
        point = Point(random.randint(0,99),random.randint(0,99))
        list.append(point)
    #retruning randomly generated list
    return list

def input_point():
    """
    this function gets the x and y
    coordinates of the input point pnew
    """
    x = int(input("enter x coordinate of new point: "))
    y = int(input("enter y coordinate of new point: "))
    p = Point(x,y)
    return p
    
def near_neigh_list():
    """
    this function finds the distance between the points
    and find the given number of nearest neighbouring points.
    """
    #getting the no of random points required from user
    ran = int(input("enter the no of randomly generated points: "))
    random_list = rand_list(ran)
    random_point = []
    #iterating the randomly generated list of points
    for j in random_list:
        random_point.append((j.x,j.y))
    #printing the randomly generated points
    print("the randomly generated points are: ",random_point)
    newp = input_point()
    #getting the no of nearest neighbouring points
    k = int(input("enter the no of nearest points: "))
    dis_list = []
    #finding the distance of the randomly generated points
    for loop in range (len(random_list)):
        dis = newp.distance(random_list[loop])
        dis_list.append(dis)
    #sorting the distances
    sorted_list = sorted(dis_list)
    neigh_list = []
    #finding the nearst points
    for distances in range (k):
        for points in range (len(sorted_list)):
            if len(neigh_list) <= k:
                #checking the distances are equal
                if sorted_list[distances] == newp.distance(random_list[points]):
                    neigh_list.append((random_list[points].x, random_list[points].y))
    #printing the nearest points
    print("the nearest points are:",neigh_list)   
if __name__ == '__main__':
    near_neigh_list()
