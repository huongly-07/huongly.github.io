class Point:
    x = int
    y = int
    
    def print_point(self):
        print("(%d,%d)" % (self.x,self.y))

A=Point()
A.x=3
A.y=4
A.print_point()

x = int(input("Nhập xB: "))
y = int(input("Nhập yB: "))
print("B",(x,y))

print("C",(-x,-y))

import math
distanceBO = math.sqrt(x**2 + y**2)
print("Distance from B to O: ",distanceBO)

distanceAB = math.sqrt((x-A.x)**2+(y-A.y)**2)
print("Distance from A to B: ",distanceAB)
