import random

RULE = 'Answer "yes" if given number is prime. Otherwise answer "no".'
MIN = 2
MAX = 50


def get_result():
    question = random.randint(MIN, MAX)

    answer = 'yes' if is_prime(question) else 'no'
    return question, answer


def is_prime(question):
    for i in range(2, int(question / 2) + 1):
        if (question % i) == 0:
            return False
    return True
