import random


RULE = 'What is the result of the expression?'
MIN = 1
MAX = 20


def get_result():
    num1 = random.randint(MIN, MAX)
    num2 = random.randint(MIN, MAX)

    operators = ['+', '-', '*']
    oper = random.choice(operators)
    arithmetic_result()
    answer = arithmetic_result()

    question = f'{num1} {oper} {num2}'
    return question, str(answer)


def arithmetic_result():
    get_result()
    num1 = get_result()
    num2 = get_result()

    if oper == '+':
        answer = num1 + num2
    elif oper == '-':
        answer = num1 - num2
    else:
        answer = num1 * num2
    return answer
