import random
from random import choice


description = 'What is the result of the expression?'


def play_game():
    first_number = random.randint(1, 100)
    second_number = random.randint(1, 100)

    operator = choice(['+', '-', '*'])

    if operator == '+':
        operation = str(first_number + second_number)
    elif operator == '-':
        operation = str(first_number - second_number)
    else:
        operation = str(first_number * second_number)

    quest = f'{first_number} {operator} {second_number}'

    return quest, operation
