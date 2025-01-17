class Rectangle:

    """
    The class is used as a basic representation of a rectangle.
    To create an instance of the rectangle, two parameters are required: width and height.
    :param width: float or integer
    :param height: float or integer

    The class has several methods, which can be used to either get information about the instance (area(), perimeter(),
    is_square()) or to alter it (resize()).
    """

    def __init__(self, width: float, height: float):
        self.width = width
        self.height = height

    def area(self) -> float:
        return self.width * self.height

    def perimeter(self) -> float:
        return (self.width + self.height) * 2

    def is_square(self) -> float:
        return self.width == self.height

    def resize(self, new_width: float, new_height: float):
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
