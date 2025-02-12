import unittest
from sources.divideNums import DivideNums  # Assuming your class is named DivideNums

class TestDivide(unittest.TestCase):
    def setUp(self):  # Correct method name is setUp, not setup_divide
        self.divideObj = DivideNums()  # Instantiate the class, not the module
    
    def test_basic_float(self):
        test1 = self.divideObj.divideTwoNums(10, 2)
        self.assertTrue(isinstance(test1, float), "Test1 Failed")  # isinstance is preferred over type()
    
    def test_decimal(self):
        test2 = self.divideObj.divideTwoNums(1, 2)
        self.assertEqual(0.5, test2, "Test2 Failed")
    
    def test_input_decimal(self):
        test3 = self.divideObj.divideTwoNums(2.2, 1.1)
        self.assertEqual(2, test3, "Test3 Failed")
    
    def test_large(self):
        test4 = self.divideObj.divideTwoNums(-200000000000000000000000000000000, -10000000000000000000000000)
        self.assertEqual(20000000, test4, "Test4 Failed")
    
    def test_zero_div(self):
        with self.assertRaises(ZeroDivisionError):  # Better context manager syntax
            self.divideObj.divideTwoNums(2, 0)
    
    def test_str_input(self):
        with self.assertRaises(TypeError):
            self.divideObj.divideTwoNums("hello", "world")
    
    def test_list_input(self):
        with self.assertRaises(TypeError):
            self.divideObj.divideTwoNums([1,2,3], [4,5,6])
