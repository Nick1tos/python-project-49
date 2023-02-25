import random

RULE = 'Answer "yes" if given number is prime. Otherwise answer "no".'
MIN = 2
MAX = 50


def get_result():
    question = random.randint(MIN, MAX)
    return question


def prime_result(question):
    answer = 'yes'
    for i in range(2, int(question / 2) + 1):
        if (question % i) == 0:
            answer = 'no'
            break
    return answer
