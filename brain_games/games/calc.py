import random


RULE = 'What is the result of the expression?'
MIN = 1
MAX = 20


def get_result():
    num1 = random.randint(MIN, MAX)
    num2 = random.randint(MIN, MAX)

    operators = ['+', '-', '*']
    oper = random.choice(operators)
    answer = arithmetic_result(num1, num2, oper)

    question = f'{num1} {oper} {num2}'
    return question, str(answer)


def arithmetic_result(num1, num2, oper):
    if oper == '+':
        answer = num1 + num2
    elif oper == '-':
        answer = num1 - num2
    else:
        answer = num1 * num2
    return answer
