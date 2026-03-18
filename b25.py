import math
class Point:
    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y

class Rectangle:
    def __init__(self, x, y, width, height):
        self.x = x              
        self.y = y
        self.width = width
        self.height = height

    def get_corners(self):
        return 
        [
            Point(self.x, self.y),
            Point(self.x + self.width, self.y),
            Point(self.x, self.y + self.height),
            Point(self.x + self.width, self.y + self.height)
        ]

class Circle:
    def __init__(self, center, radius):
        self.center = center
        self.radius = radius

def point_in_circle(circle, point):
    distance = math.sqrt((point.x - circle.center.x)**2 +
                         (point.y - circle.center.y)**2)
    return distance <= circle.radius

def rect_in_circle(circle, rect):
    for corner in rect.get_corners():
        if not point_in_circle(circle, corner):
            return False
    return True

def rect_circle_overlap(circle, rect):
    for corner in rect.get_corners():
        if point_in_circle(circle, corner):
            return True
    return False

circle = Circle(Point(150, 100), 75)
rect = Rectangle(130, 80, 50, 40)
p = Point(160, 110)

print("Point in circle:", point_in_circle(circle, p))
print("Rect in circle:", rect_in_circle(circle, rect))
print("Rect overlap circle:", rect_circle_overlap(circle, rect))