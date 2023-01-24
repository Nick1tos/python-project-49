import random

RULE = 'Answer "yes" if given number is prime. Otherwise answer "no".'


def get_numbers():
    question = random.randint(2, 50)
    for number in range(question):
        if number > 1:
            for i in range(2, question):
                if (question % 2) == 0:
                    answer = 'no'
                else:
                    answer = 'yes'
                return question, answer
