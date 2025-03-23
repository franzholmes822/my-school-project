def square_root(x):
    if x < 0:
        raise ValueError("Cannot compute square root of a negative number.")
    return x ** 0.5

try:
    print(square_root(-4))
except ValueError as e:
    print(e)
