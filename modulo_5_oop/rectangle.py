class Rectangle:
    def __init__(self, width, height):
        self.width = width
        self.height = height
    
    def area(self):
        print(f"A área é {self.width * self.height:.2f}")


retangulo = Rectangle(8.5, 12.2)
retangulo.area()
