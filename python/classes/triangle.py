class Point:
    def __init__(self, x=0.0, y=0.0):
        self.__x = x
        self.__y = y

    def getx(self):
        return self.__x

    def gety(self):
       return self.__y

    def distance_from_xy(self, x, y):
        dx = x - self.__x - x
        dy = y - self.__y - y
        return math.hypot(dx, dy)

    def distance_from_point(self, point):
        return math.hypot(self.__x - point.getx(),
                          self.__y - point.gety())


class Triangle:
    def __init__(self, vertice1, vertice2, vertice3):
        self.__points = [vertice1, vertice2, vertice3]

    def perimeter(self):
        p1, p2, p3 = self.__points
        return (p1.distance_from_point(p2) + p2.distance_from_point(p3) + p3.distance_from_point(p1))

    triangle = Triangle(Point(0,0), Point(1,0), Point(0,1))
    print(triangle.perimeter())