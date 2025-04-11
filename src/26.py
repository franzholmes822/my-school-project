def sum_of_squares(n):
    """
    Calculate the sum of squares of first n natural numbers.
    
    Parameters:
    n (int): The number of initial natural numbers to calculate the sum of squares for.
    
    Returns:
    int: The sum of squares of the first n natural numbers.
    """
    return sum(i**2 for i in range(1, n + 1))

# Example usage
result = sum_of_squares(5)
print("The sum of squares of the first 5 natural numbers is:", result)
