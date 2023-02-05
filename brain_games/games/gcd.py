import random
from math import gcd

RULE = 'Find the greatest common divisor of given numbers.'


def get_numbers():
    num1 = random.randint(1, 100)
    num2 = random.randint(1, 100)

    print('question:', num1, num2)
    answer = str(gcd(num1, num2))
    return question, answer
