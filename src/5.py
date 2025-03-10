import random

def get_random_code(length):
    alphabet = "abcdefghijklmnopqrstuvwxyz"
    return ''.join(random.choice(alphabet) for _ in range(length))

print(get_random_code(10))
