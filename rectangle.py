from point import Point


class Rectangle:
    """Represents a rectangle. attributes: width, height, corner."""

    def __init__(self):
        self.corner = Point()
        self.height = 1.0
        self.width = 1.0

    def set_basic(self, corner_x, corner_y, height, width):
        self.corner.set_coordinate(corner_x, corner_y)
        self.height = height
        self.width = width

    def move(self, dx, dy):
        self.corner.x += dx
        self.corner.y += dy

    def grow(self, dwidth, dheight):
        self.width += dwidth
        self.height += dheight
