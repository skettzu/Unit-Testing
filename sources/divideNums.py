class DivideNums:
    def divideTwoNums(num1: int, num2: int) -> float:
        if (type(num1) or type(num2)) is (str or list):
            raise TypeError
        try:
            #print(f"Number 1 is {num1} and Number 2 is {num2}")
            result = num1/num2
            return result
        except ZeroDivisionError:
            return num1/num2
    