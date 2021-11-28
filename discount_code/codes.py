import random
import string

CODE_CHARS = string.ascii_uppercase + string.digits


def generate_code(length: int = 10):
    return "".join(random.sample(CODE_CHARS, length))
