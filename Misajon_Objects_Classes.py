class Circle:
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        area = (self.radius * self.radius) * 3.14
        print("the area of the circle is ", area)


    def perimeter(self):
        perimeter = 2 * 3.14 * self.radius
        print("the perimeter of this circle is ", perimeter)



radius = Circle(eval(input("Enter a number: ")))

radius.area()
radius.perimeter()
