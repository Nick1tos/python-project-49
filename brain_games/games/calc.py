import random


RULE = 'What is the result of the expression?'
MIN = 1
MAX = 20


def get_result():
    num1 = random.randint(MIN, MAX)
    num2 = random.randint(MIN, MAX)

    operators = ['+', '-', '*']
    oper = random.choice(operators)

    question = f'{num1} {oper} {num2}'
    answer = str(answer)
    return question, answer

def arithmetic_result():
    if oper == '+':
        answer = num1 + num2
    elif oper == '-':
        answer = num1 - num2
    else:
        answer = num1 * num2
    return answer
