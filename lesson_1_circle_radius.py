import math


def calculate_circle_area(radius):

    """
    The function is used to calculate the area of the circle
    :param radius: float or integer
    :return: integer rounded to 2 decimals
    """

    area = round(math.pi * float(radius**2), 2)
    return area


while True:
    input_radius = input("Enter the radius of the circle: ")

    try:
        input_radius = float(input_radius)
        if input_radius <= 0:
            print("Please enter a number bigger than zero")
        else:
            break
    except ValueError:
        print("Please enter a number")

print(f"The area of the circle with the radius of {input_radius} cm is {calculate_circle_area(input_radius)} cm")
