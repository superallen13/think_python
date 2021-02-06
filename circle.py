import copy
from point import Point
from rectangle import Rectangle


class Circle:
    """Represents a circle. attributes: center, radius."""

    def __init__(self):
        self.center = Point()
        self.radius = 1.0
        self.cp0 = self.cp1 = self.cp2 = self.cp3 = Point()
        self.cp0.set_coordinate(0.0, 1.0)
        self.cp1.set_coordinate(1.0, 0.0)
        self.cp2.set_coordinate(0.0, -1.0)
        self.cp3.set_coordinate(-1.0, 0.0)

    def set_center_radius(self, center_x, center_y, radius):
        self.center.set_coordinate(center_x, center_y)
        self.radius = radius
        self.cp0 = self.center.move_to_new(0, self.radius)
        self.cp1 = self.center.move_to_new(self.radius, 0)
        self.cp2 = self.center.move_to_new(0, -self.radius)
        self.cp3 = self.center.move_to_new(-self.radius, 0)

    def move(self, dx, dy):
        self.set_center_radius(self.center.x + dx, self.center.y + dy, self.radius)


def distance_between_points(p1, p2):
    distance = ((p1.x - p2.x) ** 2 + (p1.y - p2.y) ** 2) ** 0.5
    return distance


def move_circle(cir, dx, dy):
    copied_cir = copy.deepcopy(cir)
    copied_cir.center.x += dx
    copied_cir.center.y += dy
    return copied_cir


def point_in_circle(cir, point):
    return distance_between_points(cir.center, point) <= cir.radius


def point_in_rect(rect, point):
    return rect.corner.x <= point.x <= rect.corner.x + rect.width and rect.corner.y \
           <= point.y <= rect.corner.y + rect.height


def rect_in_circle(cir, rect):
    p0_in_circle = point_in_circle(cir, rect.corner)
    p1_in_circle = point_in_circle(cir, rect.corner.move(0, rect.height))
    p2_in_circle = point_in_circle(cir, rect.corner.move(rect.width, rect.height))
    p3_in_circle = point_in_circle(cir, rect.corner.move(rect.width, 0))
    return p0_in_circle and p1_in_circle and p2_in_circle and p3_in_circle


def rect_circle_overlap(cir, rect):
    return point_in_rect(rect, cir.cp0) or point_in_rect(rect, cir.cp1) or \
           point_in_rect(rect, cir.cp2) or point_in_rect(rect, cir.cp3)


def main():
    circle = Circle()
    circle.set_center_radius(2.0, -1.0, 1.0)
    print(circle.cp0.x, circle.cp0.y)

    tested_rect = Rectangle()
    tested_rect.width = 6.0
    tested_rect.height = 6.0
    tested_rect.corner.x = 0.0
    tested_rect.corner.y = 0.0

    print(rect_circle_overlap(circle, tested_rect))


if __name__ == '__main__':
    main()
