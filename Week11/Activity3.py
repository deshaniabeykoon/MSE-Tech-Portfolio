import unittest

class TestStringMethods(unittest.TestCase):

    def test_upper(self):
        self.assertEqual('foo'.upper(), 'FOO') # Test if 'foo' becomes 'FOO'

    def test_isupper(self):
        self.assertTrue('FOO'.isupper())  # Test if 'FOO' is uppercase. Should return True
        self.assertFalse('Foo'.isupper())  # Test if 'Foo' is not uppercase. Should return False
        self.assertEqual('foo'.upper(), 'FOOD')  # WRONG EXPECTATION

    def test_split(self):
        s = 'hello world'   
        self.assertEqual(s.split(), ['hello', 'world']) # Test if 'hello world' splits into ['hello', 'world']`
        # check that s.split fails when the separator is not a string
        with self.assertRaises(TypeError): # Test if splitting with a non-string raises TypeError
            s.split(2)

    def test_isdigit(self):                   # Test if a string consists only of digits
        self.assertTrue('123'.isdigit())      # Checks if '123' consists only of digits
        self.assertFalse('123a'.isdigit())    # Checks if '123a' is not all digits

if __name__ == '__main__':
    unittest.main()