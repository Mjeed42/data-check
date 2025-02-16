"""Dummy challenge for Kitt Demo"""
import math


def circle_area(radius):
    """Returns the area of the circle of given radius"""
    area = math.pi * radius ** 2

    if radius <= 0:
        return  0
    else:
        return area
