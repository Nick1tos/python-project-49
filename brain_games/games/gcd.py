import random
from math import gcd

RULE = 'Find the greatest common divisor of given numbers.'
MIN = 1
MAX = 100


def get_result():
    num1 = random.randint(MIN, MAX)
    num2 = random.randint(MIN, MAX)

    question = f'{num1} {num2}'
    answer = str(gcd(num1, num2))
    return question, answer
