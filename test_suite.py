import unittest
from divideNums import divideTwoNums

def main():
    test_obj = testDivide()
    test_obj.TestNumDivision()
    

class testDivide(unittest.TestCase):
    def TestNumDivision(self):
        test1 = divideTwoNums(10,2)
        self.assertEqual(5, test1, "Test1 Failed")
        test2 = divideTwoNums(1,2)
        self.assertEqual(0.5, test2, "Test2 Failed")
        test3 = divideTwoNums(2.2,1.1)
        self.assertEqual(2, test3, "Test3 Failed")
        test4 = divideTwoNums(-200000000000000000000000000000000,-10000000000000000000000000)
        print(-200000000000000000000000000000000/-10000000000000000000000000)
        self.assertEqual(20000000, test4, "Test4 Failed")
        self.assertRaises(ZeroDivisionError, divideTwoNums, 2, 0)
        
if __name__ == '__main__':
    main()