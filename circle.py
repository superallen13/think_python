from point import Point
from rectangle import Rectangle
from rectangle import point_in_rect


class Circle:
    """Represents a circle.

    attributes: center, radius.
    methods: set_center_radius, move.
    """

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


def point_in_circle(cir, point):
    return cir.center.distance_between_points(point) <= cir.radius


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
    circle.set_center_radius(0.0, 0.0, 1.0)
    circle.cp0.get()
    circle.cp1.get()
    circle.cp2.get()
    circle.cp3.get()

    rect1 = Rectangle()
    rect1.set_basic(0, 0, 6, 6)

    rect2 = Rectangle()
    rect2.set_basic(-2, 1, 1, 3)

    print(rect_circle_overlap(circle, rect1))


if __name__ == '__main__':
    main()
