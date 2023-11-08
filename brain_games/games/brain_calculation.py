import random
from random import choice
from brain_games.games.constants import first_number_calc, second_number_calc

description = 'What is the result of the expression?'


def play_game():
    first_number = random.randint(first_number_calc, second_number_calc)
    second_number = random.randint(first_number_calc, second_number_calc)

    operator = choice(['+', '-', '*'])

    if operator == '+':
        operation = str(first_number + second_number)
    elif operator == '-':
        operation = str(first_number - second_number)
    elif operator == '*':
        operation = str(first_number * second_number)

    quest = f'{first_number} {operator} {second_number}'

    return quest, operation
