import random
import string


def generate_random_string(length, is_digits=True):
    # Get all the ASCII letters in lowercase and uppercase
    letters = string.ascii_letters

    # Randomly choose characters from letters for the given length of the string
    if is_digits:
        digits = string.digits
        return "".join(random.choice(letters + digits) for i in range(length))
    return "".join(random.choice(letters) for i in range(length))
