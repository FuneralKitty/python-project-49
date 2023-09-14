import random
from random import choice

DESCRIPTION = 'What is the result of the expression?'


def play_game():
    number1 = random.randint(1, 100)
    number2 = random.randint(1, 100)

    operator = choice(["+", "-", "*"])

    if operator == '+':
        operation = str(number1 + number2)
    elif operator == '-':
        operation = str(number1 - number2)
    else:
        operation = str(number1 * number2)

    quest = f"{number1} {operator} {number2}"

    return quest, operation
