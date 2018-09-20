def is_equilateral(sides):
    return sides[0] == sides[1] == sides[2] and triangle_properties(sides)


def is_isosceles(sides):
    return (sides[0] == sides[1] or sides[0] == sides[2] or sides[1] == sides[2]) and triangle_properties(sides)


def is_scalene(sides):
    return sides[0] != sides[1] != sides[2] and triangle_properties(sides)


def triangle_properties(sides):
    return sum(sides) / 2 > max(sides)
