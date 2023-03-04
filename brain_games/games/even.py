import random


RULE = 'Answer "yes" if the number is even, otherwise answer "no".'
MIN = 1
MAX = 100


def get_result():
    question = random.randint(MIN, MAX)

    if even_result(question):
        answer = 'yes'
    else:
        answer = 'no'
    return question, answer


def even_result(question):
    if question % 2:
        return False
    else:
        return True
