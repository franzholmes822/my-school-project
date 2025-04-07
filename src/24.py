def add_numbers(a: float, b: float) -> float:
    """
    This function takes two numbers as input and returns their sum.
    
    Example usage:
    >>> add_numbers(2.5, 4.3)
    6.8
    
    >>> add_numbers(-1.0, -3.0)
    -4.0
    """
    return a + b

def calculate_expression(expression: str) -> float:
    """
    This function takes an arithmetic expression as input and returns the result.
    
    Example usage:
    >>> calculate_expression("2 + 5 * 3")
    13
    
    >>> calculate_expression("-4 - 6 / 2")
    -7.0
    """
    return eval(expression)

def main():
    a = float(input("Enter the first number: "))
    b = float(input("Enter the second number: "))

    # Example usage with user-defined functions
    sum_result = add_numbers(a, b)
    print(f"The sum of {a} and {b} is {sum_result}")

    expression = input("Enter an arithmetic expression: ")
    result = calculate_expression(expression)
    print(f"The result of the expression '{expression}' is {result:.2f}")

if __name__ == "__main__":
    main()
