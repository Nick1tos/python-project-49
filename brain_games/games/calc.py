import random

RULE = 'What is the result of the expression?'


def get_numbers():
    num1 = random.randint(1, 20)
    num2 = random.randint(1, 20)

    operators = ['+', '-', '*']
    oper = random.choice(operators)

    question = f'{num1} {oper} {num2}'

    if oper == '+':
        answer = num1 + num2
    elif oper == '-':
        answer = num1 - num2
    else:
        answer = num1 * num2
    answer = str(answer)
    return question, answer
