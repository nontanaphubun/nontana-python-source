"""
Write a Python class Rectangle with:

Private attributes for length and width
Methods to calculate area (getArea()) and perimeter getPerimeter())
A method to check if it's a square (isSquare())

"""
class Rectangle:
    def __init__(self, lenght, width):
        self.__lenght = length
        self.__width = width

    def getArea(sefe):
        return self.__length * self.__width
    
    def getPerimeter(sefe):
        return 2 * (self.__lenght + self.__width)
    
    def isSquare(self)
        if self.__lengh == self.__width:
            return True
        else:
            return False
x = Rectangle(10,5)
print(f"Area of x = { x.getArea()}")
print(f"Perimeter of x = { x.getPerimeter()}")

if x.isSquare:
    print("x is square")
else:
    print("x is not square")