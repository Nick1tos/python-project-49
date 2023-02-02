import random

RULE = 'Answer "yes" if given number is prime. Otherwise answer "no".'


def get_numbers():
    question = random.randint(2, 50)
    answer = 'yes'
    for i in range(2, int(question / 2) + 1):
        if (question % i) == 0:
            answer = 'no'
            break
    return question, answer
