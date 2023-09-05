import random
from brain_games.games.cli import welcome_user
from brain_games.games.engine import (
    congratulation,
    get_user_response,
    print_question,
    print_correct_answer,
    print_wrong_answer_calculation,
)


def is_prime_logic(number):
    if number <= 1:
        return "no"
    if number == 2:
        return "yes"
    for i in range(2, number):
        if number % i == 0:
            return "no"
    return "yes"


def random_generator():
    random_num = random.randint(1, 100)
    random_num_2 = random.randint(1, 100)
    return random_num, random_num_2


def play_game():
    input_name = welcome_user()
    print('Answer "yes" if given number is prime. Otherwise answer "no".')
    user_score = 0
    while user_score < 3:
        num, _ = random_generator()

        print_question(f"{num}")
        user_response = get_user_response()
        print('Your answer:', user_response)
        expected_result = is_prime_logic(num)
        if user_response == str(expected_result):
            print_correct_answer()
            user_score += 1
        else:
            print_wrong_answer_calculation(
                user_response, expected_result, input_name)
            break

    if user_score == 3:
        congratulation(input_name)
