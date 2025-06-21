import random


def get_random_code(nubmer):
    code = ""
    for _ in range(0, nubmer):
        code = code + str(random.randint(0, 9))
    return code
