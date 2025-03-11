import numpy as np
def get_random_code(length):
    """Generates a random string of letters and digits.

    Parameters:
        length (int): The desired length of the string.

    Returns:
        str: A random string of letters and digits of the specified length.
    """
    return ''.join(np.random.choice(list('abcdefghijklmnopqrstuvwxyz' +
                                       'ABCDEFGHIJKLMNOPQRSTUVWXYZ' +
                                       '0123456789'), length))
