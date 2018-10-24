import math

class Rectangle(object):
    def __init__(self, width, height):
        self.width = width
        self.height = height
    def area(self):
        return self.width * self.height

class Square(Rectangle):
    def __init__(self, width):
        self.width  = width
        self.height = width

class Ellipse (object):
    def __init__(self,real_axis,imaginary_axis):
        self.real_axis = real_axis
        self.imaginary_axis = imaginary_axis
    def area(self):
        return math.pi*self.real_axis*self.imaginary_axis

class Circle (Ellipse):
    def __init__(self, radius):
        self.real_axis = radius
        self.imaginary_axis = radius

def compute_area(shapes):
    return sum(x.area()for x in shapes)
    
shapes = [Ellipse(10, 20), Square(15), Circle(5),Rectangle(20, 15), Circle(5), Square(15),Ellipse(10, 20)]
total_area = compute_area(shapes)
print(total_area) 
