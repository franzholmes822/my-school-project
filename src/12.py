import math

def calculate_pi(n):
    x = 0
    y = 0
    inside = 0
    for i in range(n):
        x = random.random() * 2 - 1
        y = random.random() * 2 - 1
        if x ** 2 + y ** 2 <= 1:
            inside += 1
    return 4 * inside / n
