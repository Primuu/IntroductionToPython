# Task 1
class Point:

    def __init__(self, x: int = 0, y: int = 0):
        self.x = x
        self.y = y

    # Task 2
    def __str__(self):
        return f'Point({self.x}, {self.y})'

    # Task 3
    def __mul__(self, other):
        return Point(self.x * other, self.y * other)

    # Task 4
    def __eq__(self, other):
        if isinstance(other, self.__class__):
            return other.x == self.x and other.y == self.y
        return False

    # Task 6
    def __repr__(self):
        return f'Point({self.x}, {self.y})'


# Task 1
p1: Point = Point()
print(p1.__dict__)

# Task 2
print(p1)

# Task 3
p2: Point = Point(1, 3)
print(p2 * 5)  # before: TypeError: unsupported operand type(s) for *: 'Point' and 'int'

# Task 4
a = 5
print(p1 == p1)
print(p1 == p2)
print(a == p1)


# Task 5

class Polygon:

    def __init__(self):
        self.points = []

    def add_point(self, point: Point):
        self.points.append(point)

    # Task 6
    def __str__(self):
        return f'Polygon{self.points}'

    # Task 7
    def __getitem__(self, item):
        if isinstance(item, int) or isinstance(item, slice):
            return self.points[item]
        else:
            raise TypeError("Item must be an int or slice")


# Task 5
polygon: Polygon = Polygon()
polygon.add_point(p2)
print(polygon.points)

# Task 6
p3: Point = Point(2, 3)
p4: Point = Point(1, 1)
polygon2: Polygon = Polygon()
polygon2.add_point(p1)
polygon2.add_point(p2)
polygon2.add_point(p3)
polygon2.add_point(p4)
print(polygon2)

# Task 7
# print(polygon2[0.3])  # TypeError: Item must be an int or slice
print(polygon2[0])
print(polygon2[1: 3])
