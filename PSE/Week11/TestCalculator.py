import unittest  
from calculator import add, subtract, multiply, divide, root, power, sin, cos, tan

# Test cases for the calculator functions
# Each function tests a specific operation of the calculator

class TestMathOperations(unittest.TestCase):  # Test class inheriting from unittest.TestCase
    
    def test_add(self):                       # Test "add"
        self.assertEqual(add(2, 3), 5)        # Test  2 + 3 = 5
        self.assertEqual(add(-1, 1), 0)       # Test -1 + 1 = 0 (negative number)

    def test_subtract(self):                 # Test "subtract"
        self.assertEqual(subtract(10, 5), 5) # Test 10 - 5 = 5
        self.assertEqual(subtract(5, 10), -5)# Test 5 - 10 = -5 (negative result)
        self.assertEqual(subtract(0, 0), 0)  # Test 0 - 0 = 0 (zero result)

    def test_multiply(self):                 # Test "multiply"
        self.assertEqual(multiply(3, 4), 12) # Test 3 * 4 = 12
        self.assertEqual(multiply(0, 5), 0)  # Test 0 * 5 = 0 (multiplication by zero)      
        self.assertEqual(multiply(-1, 5), -5)# Test -1 * 5 = -5 (negative number)

    def test_divide(self):                   # Test "divide"
        self.assertEqual(divide(10, 2), 5)   # Test 10 / 2 = 5
        self.assertEqual(divide(9, 3), 3)    # Test 9 / 3 = 3
        with self.assertRaises(ValueError):  # Test division by zero raises ValueError
            divide(10, 0)                    # Expecting ValueError when dividing by zero

    def test_root(self):                     # Test "root"
        self.assertEqual(root(4), 2)         # Test square root of 4 is 2
        self.assertEqual(root(0), 0)         # Test square root of 0 is 0
        self.assertEqual(root(27, 3), 3)     # Test cube root of 27 is 3
        with self.assertRaises(ValueError):  # Test square root of negative number raises ValueError
            root(-1)                         # Expecting ValueError when computing square root of negative number

    def test_power(self):                    # Test "power"
        self.assertEqual(power(2, 3), 8)     # Test 2 raised to the power of 3 is 8
        self.assertEqual(power(5, 0), 1)     # Test any number raised to the power of 0 is 1
        self.assertEqual(power(3, -1), 1/3)  # Test negative exponent (3^-1 = 1/3)

    def test_trigonometric_sine(self):                     # Test "sine"
        self.assertAlmostEqual(sin(0), 0)                  # Test sine of 0 degrees is 0
        self.assertAlmostEqual(sin(30), 0.5, places=2)     # Test sine of 30 degrees is 0.5
        self.assertAlmostEqual(sin(90), 1)                 # Test sine of 90 degrees is 1
        self.assertAlmostEqual(sin(180), 0, places=2)      # Test sine of 180 degrees is 0
        self.assertAlmostEqual(sin(270), -1, places=2)     # Test sine of 270 degrees is -1
        self.assertAlmostEqual(sin(360), 0, places=2)      # Test sine of 360 degrees is 0

    def test_trigonometric_cosine(self):                  # Test "cosine"
        self.assertAlmostEqual(cos(0), 1)                 # Test cosine of 0 degrees is 1
        self.assertAlmostEqual(cos(60), 0.5, places=2)    # Test cosine of 60 degrees is 0.5
        self.assertAlmostEqual(cos(90), 0, places=2)      # Test cosine of 90 degrees is 0
        self.assertAlmostEqual(cos(180), -1)              # Test cosine of 180 degrees is -1
        self.assertAlmostEqual(cos(360), 1)               # Test cosine of 360 degrees is 1

    def test_trigonometric_tangent(self):                 # Test "tangent"
        self.assertAlmostEqual(tan(0), 0)                 # Test tangent of 0 degrees is 0
        self.assertAlmostEqual(tan(45), 1, places=2)      # Test tangent of 45 degrees is 1
        self.assertAlmostEqual(tan(180), 0, places=2)     # Test tangent of 180 degrees is 0
        with self.assertRaises(ValueError):               # Test undefined tangent
            tan(90)
        with self.assertRaises(ValueError):              # Test another undefined angle
            tan(270)

if __name__ == '__main__':                   # Main block to run the tests                            
    unittest.main()
