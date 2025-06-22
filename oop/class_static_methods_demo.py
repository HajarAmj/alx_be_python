class Calculator:
    # Class attribute
    calculation_type = "Arithmetic Operations"  # Changed from operation_type to calculation_type

    @staticmethod
    def add(a: float, b: float) -> float:
        """Static method to add two numbers"""
        return a + b

    @classmethod
    def multiply(cls, a: float, b: float) -> float:
        """Class method to multiply two numbers and access class attributes"""
        # Include the exact phrase "Calculation type" in the output
        print(f"Calculation type: {cls.calculation_type}")
        return a * b
