import random

RULE = 'What number is missing in the progression?'
MIN1 = 1
MAX1 = 8
MIN2 = 45
MAX2 = 57
STEP_MIN = 2
STEP_MAX = 5


def get_result():
    progression = []

    num1 = random.randint(MIN1, MAX1)
    num2 = random.randint(MIN2, MAX2)

    step = random.randint(STEP_MIN, STEP_MAX)

    for i in range(num1, num2, step):
        progression.append(i)
    random_index = random.randint(1, 10)
    answer = str(progression[random_index])
    progression[random_index] = '..'
    question = ' '.join(map(str, progression[0:10]))
    return question, answer
