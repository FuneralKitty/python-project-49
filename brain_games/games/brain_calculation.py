import random
from brain_games.games.cli import welcome_user
from brain_games.games.engine import (
    congratulation,
    get_user_response,
    print_question,
    print_correct_answer,
    print_wrong_answer,
)


def perform_operation(operation, number1, number2):
    if operation == '+':
        return number1 + number2
    elif operation == '-':
        return number1 - number2
    else:
        return number1 * number2


def controlled_operation(operation_counter):
    if operation_counter == 0:
        return '+'
    elif operation_counter == 1:
        return '-'
    else:
        return '*'


def play_game():
    input_name = welcome_user()
    print("What is the result of the expression?")
    user_score = 0
    operation_counter = 0

    while user_score < 3:
        number1 = random.randint(1, 100)
        number2 = random.randint(1, 100)
        operation = controlled_operation(operation_counter)

        print_question(f"{number1} {operation} {number2}")
        expected_result = perform_operation(operation, number1, number2)

        user_response = get_user_response()
        print('Your answer:', user_response)

        if str(expected_result) == user_response:
            print_correct_answer()
            user_score += 1
            operation_counter += 1
        else:
            print_wrong_answer(user_response, input_name)
            break

    if user_score == 3:
        congratulation(input_name)
