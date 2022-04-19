import math


class Point:
    """Represents a point in 2-D space.

    attributes: x, y
    """
    def __init__(self,x,y):
        self.x=x
        self.y=y
    



michael = Point()
# creating an object/instance using initializer/constructer, realization

michael.x = 3
michael.y = 4
print(type(michael))

victor = Point()
victor.x = 6
victor.y = 8
print(victor.x)
print(victor.y)
print(victor)



def print_point(p):
    """Print a Point object in human-readable format.

    p: a Point object
    """
    print(f'({p.x}, {p.y})')


print_point(michael)
print_point(victor)


def distance_between_points(p1, p2):
    """Computes the distance between two Point objects.

    p1: Point
    p2: Point


    returns: float
    distance between points = sqrt ( square of (distance between x's) + square of (distance between y's) )
    """
    d_x = p1.x - p2.x
    d_y = p1.y - p2.y
    d = math.sqrt(d_x ** 2 + d_y ** 2)
    return d

print(distance_between_points(michael, victor))


class Rectangle:
    """Represents a rectangle.

    attributes: width, height, corner.
    """


box = Rectangle() # creating an object of Rectangle
box.width = 100.0
box.height = 200.0
box.corner = Point() 
box.corner.x = 0.0
box.corner.y = 0.0    

def find_center(rect):
    """Returns a Point at the center of a Rectangle.

    rect: Rectangle

    returns: new Point
    """
    p = Point()
    p.x = rect.corner.x + rect.width / 2
    p.y = rect.corner.y + rect.height / 2
    return p


center_box = find_center(box)
print(type(center_box))
print_point(center_box)