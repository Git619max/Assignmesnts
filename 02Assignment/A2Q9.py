def area_tri(base, height):
    return 0.5*base*height
def area_rect(length, breadth):
    return length*breadth
def area_circle(radius):
    return 3.14*radius*radius
def area_rhombus(base, height):
    return base*height
print("Area of triangle with base = 10, height = 10 :",area_tri(10,10))
print("Area of rectangle with length = 10 and breadth = 15 :",area_rect(10,15))
print("Area of square with side = 10 :",area_rect(10,10))
print("Area of circle with radius = 10 :",area_circle(10))
print("Area of rhombus with base = 10, height = 10 :",area_rhombus(10,10))