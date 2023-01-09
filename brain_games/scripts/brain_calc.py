import prompt
import random


def main():
    print('Welcome to the Brain Games!')
    i = 0
    name = prompt.string('May I have your name? ')
    print(f'Hello, {name}!\nWhat is the result of the expression?')
    while i < 3:
        operators = ['+', '-', '*']
        oper = random.choice(operators)
        num1 = random.randint(1, 20)
        num2 = random.randint(1, 20)
        print(f'Question: {num1} {oper} {num2}')
        answer = prompt.string('Your answer: ')
        if oper == '+':
            result = num1 + num2
        elif oper == '-':
            result = num1 - num2
        else:
            result = num1 * num2
        if int(result) == int(answer):
            print('Correct')
        else:
            print(f"{answer} is wrong answer ;(. Correct answer "
                  f"was {result}.\nLet`s try again, {name}")
            break
        i += 1
    if i == 3:
        print(f'Congratulations, {name}')


if __name__ == '__main__':
    main()
