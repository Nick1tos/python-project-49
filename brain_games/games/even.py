import random


RULE = 'Answer "yes" if the number is even, otherwise answer "no".'
MIN = 1
MAX = 100


def get_result():
    question = random.randint(MIN, MAX)

    answer = 'yes' if is_even(question) else 'no'
    return question, answer


def is_even(question):
    if question % 2:
        return False
    else:
        return True
