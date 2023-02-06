import random

RULE = 'What number is missing in the progression?'


def get_numbers():
    progression = []

    num1 = random.randint(1, 8)
    num2 = random.randint(45, 57)

    step = random.randint(2, 5)

    for i in range(num1, num2, step):
        progression.append(i)
    random_index = random.randint(1, 10)
    answer = str(progression[random_index])
    progression[random_index] = '..'
    question = ' '.join(map(str, progression[1:10]))
    return question, answer
