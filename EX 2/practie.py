class Point():
    x = 0
    y = 0
    def __init__ (self, a, b):
        self.x = a
        self.y = b
    def distance(self, other):
        x_diff = (self.x - other.x) ** 2
        y_diff = (self.y - other.y) ** 2
        dis_btw = (x_diff + y_diff) ** 0.5
        return dis_btw
    def sum_point(self, other):
        x_sum = self.x + other.x
        y_sum = self.y + other.y
        sum_points = (x_sum, y_sum)
        return sum_points
    def sub_point(self, other):
        x_sub = self.x - other.x
        y_sub = self.y - other.y
        sub_points = (x_sub, y_sub)
        return sub_points

point_list = []
ran = int(input("enter  the no of points : "))
for points in range(ran):
    x_value = int(input("enter the x coordinate : "))
    y_value = int(input("enter the y coordinate : "))
    point = Point(x_value, y_value)
    point_list.append(point)
print(point_list[0].distance(point_list[1]))