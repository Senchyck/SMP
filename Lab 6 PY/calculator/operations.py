class Calculator:
    @staticmethod
    def validate_numbers(a, b):
        if not (isinstance(a, (int, float)) and isinstance(b, (int, float))):
            raise ValueError("Invalid number")

    @staticmethod
    def add(a, b):
        Calculator.validate_numbers(a, b)
        return a + b

    @staticmethod
    def subtract(a, b):
        Calculator.validate_numbers(a, b)
        return a - b

    @staticmethod
    def multiply(a, b):
        Calculator.validate_numbers(a, b)
        return a * b

    @staticmethod
    def divide(a, b):
        Calculator.validate_numbers(a, b)
        if b == 0:
            raise ValueError("Cannot divide by zero")
        return a / b
