import math

def area(radius):
    if radius <= 0:
        return "invalid radius"
    else:
        return math.pi * radius ** 2

def circumference(radius):
    if radius <= 0:
        return "invalid radius"
    else:
        return 2 * math.pi * radius
