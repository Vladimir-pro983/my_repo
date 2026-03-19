import math


def square(side):
    area = side * side
    return math.ceil(area)


# примеры
print(square(4))
print(square(4.2))
