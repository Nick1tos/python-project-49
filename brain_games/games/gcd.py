import random
from math import gcd

RULE = 'Find the greatest common divisor of given numbers.'


def get_numbers():
    num1 = random.randint(1, 100)
    num2 = random.randint(1, 100)

    question = f'{num1}, {num2}'
    answer = str(gcd(num1, num2))

    return question, answer

    """if math.gcd(num1, num2):
        answer = math.gcd"""
    """answer = math.gcd(num1, num2)"""
    """if num1 < num2:
        num1, num2 = num2, num1

    while num2 != 0:
        num1, num2 = num2, num1 % num2"""

    """, num1"""

