import math

class MathProcessor:
    def __init__(self, input_value):
        self.result = 0
        self.input_value = input_value
        self.diameter = 0

    def calculate_sin_cos(self):
        """Calculate the sine and cosine of the input value."""
        if self.input_value < 0:
            raise ValueError("Input value cannot be negative.")
        self.result = math.sin(self.input_value) + math.cos(self.input_value)
        print(f"sin({self.input_value}) + cos({self.input_value}) = {self.result}")

    def calculate_sin(self, angle):
        """Calculate the sine of an angle in degrees."""
        if angle < 0:
            raise ValueError("Angle cannot be negative.")
        return math.sin(math.radians(angle))
    
    def calculate_cos(self, angle):
        """Calculate the cosine of an angle in degrees."""
        if angle < 0:
            raise ValueError("Angle cannot be negative.")
        return math.cos(math.radians(angle))

    def area_circle(self, diameter):
        """Calculate the area of a circle given its diameter."""
        if diameter < 0:
            raise ValueError("Diameter cannot be negative.")
        radius = diameter / 2
        return math.pi * (radius ** 2)
    
    def area_rectangle(self, length, width):
        """Calculate the area of a rectangle given its length and width."""
        if length < 0 or width < 0:
            raise ValueError("Length and width cannot be negative.")
        return length * width
    
    def area_triangle(self, base, height):
        """Calculate the area of a triangle given its base and height."""
        if base < 0 or height < 0:
            raise ValueError("Base and height cannot be negative.")
        return 0.5 * base * height
    
    def calculate_area(self, shape, *args):
        """Calculate the area of a given shape."""
        match shape.lower():
            case "circle":
                if len(args) != 1:
                    raise ValueError("Circle requires one argument: diameter.")
                return self.area_circle(args[0])
            case "rectangle":
                if len(args) != 2:
                    raise ValueError("Rectangle requires two arguments: length and width.")
                return args[0] * args[1]
            case "triangle":
                if len(args) != 2:
                    raise ValueError("Triangle requires two arguments: base and height.")
                return 0.5 * args[0] * args[1]
            case _:
                raise ValueError("Unsupported shape. Please use 'circle', 'rectangle', or 'triangle'.")