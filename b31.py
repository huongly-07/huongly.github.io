import copy
class Point:
    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y
    def __str__(self):
        return f"({self.x},{self.y})"

class LineSegment:
    def __init__(self, *args):
        self.__d1 = None
        self.__d2 = None

        if len(args) == 0:
            self.__d1 = Point(8, 5)
            self.__d2 = Point(1, 0)

        elif len(args) == 2 and isinstance(args[0], Point):
            self.__d1 = args[0]
            self.__d2 = args[1]

        elif len(args) == 4:
            self.__d1 = Point(args[0], args[1])
            self.__d2 = Point(args[2], args[3])

        elif len(args) == 1 and isinstance(args[0], LineSegment):
            self.__d1 = copy.deepcopy(args[0].get_d1())
            self.__d2 = copy.deepcopy(args[0].get_d2())

    def get_d1(self): return self.__d1
    def get_d2(self): return self.__d2

    def __str__(self):
        return f"LineSegment[d1={self.__d1}, d2={self.__d2}]"

s1 = LineSegment()
print(f"Mặc định: {s1}")

p1 = Point(3, 3)
p2 = Point(7, 7)
s2 = LineSegment(p1, p2)
print(f"Dùng Point: {s2}")

s3 = LineSegment(10, 20, 30, 40)
print(f"Dùng 4 số: {s3}")

s4 = LineSegment(s3)
print(f"Sao chép từ ls3: {s4}") 
   

   
   
        
 

