import random


RULE = 'Answer "yes" if the number is even, otherwise answer "no".'
MIN = 1
MAX = 100


def get_result():
    question = random.randint(MIN, MAX)

    if question % 2 == 0:
        answer = 'yes'
    else:
        answer = 'no'
    return question, answer
