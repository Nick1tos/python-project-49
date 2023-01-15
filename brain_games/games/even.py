import random

RULE = 'Answer "yes" if the number is even,otherwise answer "no".'


def get_numders():
    question = random.randint(1, 100)

    if question % 2 == 0:
        answer = 'yes'
    else:
        answer = 'no'
    return question, answer