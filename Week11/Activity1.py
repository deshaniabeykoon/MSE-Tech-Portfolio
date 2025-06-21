import unittest

def add(x, y):
    return x + y

# TestMathOperations is a class that inherits from unittest.TestCase
# it contains test cases for the add function.
# It uses the unittest framework to check if the add function works correctly.
class TestMathOperations(unittest.TestCase):
    # Test case for the add function
    # This test checks if the add function correctly adds two numbers.
    # It uses unittest framework to assert the expected output.
    def test_add(self):
        self.assertEqual(add(2, 3), 5)
        self.assertEqual(add(-1, 1), 0)

if __name__ == '__main__':
    unittest.main()
