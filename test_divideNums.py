import unittest
from divideNums import divideTwoNums
import dataclasses
'''
def main():
    test_obj = testDivide()
    test_obj.TestNumDivision()
'''

@dataclasses
class testDivide(unittest.TestCase):
    def test_basic_float(self):
        test1 = divideTwoNums(10,2)
        self.assertTrue(type(test1) is float, "Test1 Failed")

    def test_decimal(self):
        test2 = divideTwoNums(1,2)
        self.assertEqual(0.5, test2, "Test2 Failed")

    def test_input_decimal(self):
        test3 = divideTwoNums(2.2,1.1)
        self.assertEqual(2, test3, "Test3 Failed")

    def test_large(self):
        test4 = divideTwoNums(-200000000000000000000000000000000,-10000000000000000000000000)
        self.assertEqual(20000000, test4, "Test4 Failed")

    def test_zero_div(self):
        self.assertRaises(ZeroDivisionError, divideTwoNums, 2, 0)

    def test_str_input(self):
        self.assertRaises(TypeError, divideTwoNums, "hello", "world")

    def test_list_input(self):
        self.assertRaises(TypeError, divideTwoNums, [1,2,3], [4,5,6])
        
if __name__ == '__main__':
    pass
    #main()