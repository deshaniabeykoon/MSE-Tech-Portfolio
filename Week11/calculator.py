import math

def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b):
    if b == 0:
        raise ValueError("Cannot divide by zero")
    return a / b

def power(a, b):
    return a ** b

def root(a, n):
    if a < 0 and n % 2 == 0:
        raise ValueError("Cannot take even root of a negative number.")
    return a ** (1 / n)

def sin(angle_rad):
    return math.sin(angle_rad)

def cos(angle_rad):
    return math.cos(angle_rad)

def tan(angle_rad):
    return math.tan(angle_rad)
