class Rectangle:

    def __init__(self, width: float, height: float):
        self.width = width
        self.height = height

    def area(self):
        return self.width * self.height

    def perimeter(self):
        return (self.width + self.height) * 2

    def is_square(self):
        return True if self.width == self.height else False

    def resize(self, new_width, new_height):
        self.width = new_width
        self.height = new_height


##################
# Testing ground #
##################

rectangle_1 = Rectangle(5, 10)

print(rectangle_1.width, rectangle_1.height)
print(rectangle_1.perimeter(), rectangle_1.area())
print(rectangle_1.is_square())

rectangle_1.resize(15, 15)

print(rectangle_1.width, rectangle_1.height)
print(rectangle_1.perimeter(), rectangle_1.area())
print(rectangle_1.is_square())
