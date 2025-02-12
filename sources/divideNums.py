class DivideNums:
    def divideTwoNums(self, num1, num2) -> float:
        # Check for invalid types
        if isinstance(num1, (str, list)) or isinstance(num2, (str, list)):
            raise TypeError("Inputs must be numbers")
        
        # The division will naturally raise ZeroDivisionError
        # No need to catch and re-raise it
        result = float(num1) / num2
        return result
