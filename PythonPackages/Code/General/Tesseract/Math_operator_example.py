class MathOperations:
    """
    A class that provides basic math operations like addition, subtraction,
    multiplication, and division.
    """

    def add(self, a, b):
        """
        Add two numbers and return the result.

        :param a: The first number to be added.
        :param b: The second number to be added.
        :return: The sum of a and b.
        """
        return a + b

    def subtract(self, a, b):
        """
        Subtract one number from another and return the result.

        :param a: The number to be subtracted from.
        :param b: The number to subtract.
        :return: The result of a minus b.
        """
        return a - b

    def multiply(self, a, b):
        """
        Multiply two numbers and return the result.

        :param a: The first number to be multiplied.
        :param b: The second number to be multiplied.
        :return: The product of a and b.
        """
        return a * b

    def divide(self, a, b):
        """
        Divide one number by another and return the result.

        :param a: The dividend.
        :param b: The divisor.
        :return: The result of a divided by b.
        :raises ZeroDivisionError: If b is zero.
        """
        if b == 0:
            raise ZeroDivisionError("Cannot divide by zero.")
        return a / b

# Example usage of the MathOperations class
if __name__ == "__main__":
    math_ops = MathOperations()

    # Add two numbers
    result_add = math_ops.add(5, 3)
    print(f"Addition Result: {result_add}")

    # Subtract two numbers
    result_sub = math_ops.subtract(5, 3)
    print(f"Subtraction Result: {result_sub}")

    # Multiply two numbers
    result_mul = math_ops.multiply(5, 3)
    print(f"Multiplication Result: {result_mul}")

    # Divide two numbers
    try:
        result_div = math_ops.divide(5, 0)
        print(f"Division Result: {result_div}")
    except ZeroDivisionError as e:
        print(e)
