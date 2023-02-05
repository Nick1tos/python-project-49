"""General logic for all games"""

import prompt

MAX_ROUNDS = 3


def play(game):
    print('Welcome to the Brain Games!')
    name = prompt.string('May I have your name? ')
    print(f'Hello, {name}')

    print(game.RULE)

    for _ in range(MAX_ROUNDS):
        question, answer = game.get_numbers()

        print(f'Question: {question}')
        user_answer = prompt.string('Your answer: ')

        if user_answer == answer:
            print('Correct!')
        else:
            print(f"{user_answer} is wrong answer ;(. Correct answer "
                  f"was {answer}.\nLet`s try again, {name}!")
            break
    else:
        print(f'Congratulations, {name}!')
