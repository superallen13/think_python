import copy


class Point:
    """Represents a point in 2-D space.

    attributes: x, y.
    method: set_coordinate, get, move_to_new, distance_between_points.
    """

    def __init__(self):
        self.x = 0.0
        self.y = 0.0

    def set_coordinate(self, x, y):
        self.x = x
        self.y = y

    def get(self):
        coordinate = (self.x, self.y)
        print(coordinate)
        return coordinate

    def move_to_new(self, dx, dy):
        copied_point = copy.deepcopy(self)
        copied_point.x += dx
        copied_point.y += dy
        return copied_point

    def distance_between_points(self, point):
        return ((self.x - point.x) ** 2 + (self.y - point.y) ** 2) ** 0.5
