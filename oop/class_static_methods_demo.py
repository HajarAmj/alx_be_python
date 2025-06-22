class Calculator:
    # Class attribute
    operation_type = "Arithmetic Operations"

    @staticmethod
    def add(a: float, b: float) -> float:
        """Static method to add two numbers"""
        return a + b

    @classmethod
    def multiply(cls, a: float, b: float) -> float:
        """Class method to multiply two numbers and access class attributes"""
        print(f"Calculation type: {cls.operation_type}")
        return a * b